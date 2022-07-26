import concurrent.futures
import json
import logging
import os
from concurrent.futures import as_completed
from typing import Callable, List

from tqdm.auto import tqdm

from .common import find_project_and_institutes
from ..services.entities import ApiClient
from ..services.entities.model.file import File
from ..services.entities.model.root_study import RootStudy

logger = logging.getLogger(__name__)


def download_institutes(project_name: str, institute_name: str, destination: str, categories: List[str] = None,
                        studies_filter: Callable[[RootStudy], bool] = None,
                        files_filter: Callable[[File, RootStudy], bool] = None, include_modified_date = False):
    project, institutes = find_project_and_institutes(project_name, institute_name)
    if not project:
        logger.error(f"Project not found: {project_name}")
        return

    if not institutes:
        logger.error(f"No institutes found")
        return

    for institute in tqdm(institutes, desc="Institutes", unit="Institute"):
        logger.info(f"Institute name: {institute.name}, project type: {project.project_type_name}, "
                    f"destination: {destination}")
        logger.debug(f"Institute id: {institute.id} and project id: {project.id}")

        studies = institute.studies

        if callable(studies_filter):
            studies = list(filter(studies_filter, studies))

        categories = [category for category in categories or [] if category in ['files', 'dicom', 'annotations']]
        if not categories:
            categories = ['files']

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            with tqdm(total=len(studies), desc="Studies", unit='study') as pbar:
                fs = {executor.submit(_download_study, study, os.path.join(destination, institute.name,
                                                                           study.study_id_human_readable),
                                      categories, files_filter, include_modified_date): study for study in studies}
                for future in as_completed(fs):
                    study = fs.pop(future)
                    pbar.update()
                    try:
                        future.result()
                        logger.debug(f"Downloaded: {study.study_id_human_readable}")
                    except Exception:
                        logger.exception(f"Exception during download of {study.study_id_human_readable}")


def _download_study(study, study_destination, categories, files_filter, include_modified_date):
    study_json_file = os.path.join(study_destination, 'study.json')
    os.makedirs(os.path.dirname(study_json_file), exist_ok=True)
    with open(study_json_file, 'w') as f:
        json.dump(ApiClient.sanitize_for_serialization(study), f, indent=4)

    files = list()
    for category in categories:
        files.extend(getattr(study, category).copy())
    if callable(files_filter):
        files = list(filter(lambda file: files_filter(file, study), files))

    total_size = sum([file.file_size for file in files if file.is_completed])

    def study_destination_fn(file: File) -> str:
        if len(categories) > 1:
            return os.path.join(study_destination, file.category)
        return study_destination

    with concurrent.futures.ThreadPoolExecutor() as executor:
        fs = {executor.submit(file.download, study_destination_fn(file), overwrite=False,
                              include_modified_date=include_modified_date): file for file in files}
        study_folder = os.path.basename(study_destination)
        with tqdm(total=total_size, leave=False, desc=f"Study {study_folder}", unit='B', unit_scale=True,
                  unit_divisor=1024) as pbar:
            for future in as_completed(fs):
                file = fs.pop(future)
                pbar.update(file.file_size)
                try:
                    downloaded = future.result()
                    if downloaded:
                        logger.debug(f"Downloaded: {file.file_name}")
                    else:
                        logger.debug(f"Skipped: {file.file_name}")
                except Exception:
                    logger.exception(f"Exception during download of {file.file_name}")
