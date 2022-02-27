import concurrent.futures
import logging
import os
from concurrent.futures import as_completed
from typing import Callable

from tqdm.auto import tqdm

from .common import find_project_by_name, find_institute_by_name
from ..services.entities.model.file import File
from ..services.entities.model.root_study import RootStudy

logger = logging.getLogger(__name__)


def download_institute(project_name: str, institute_name: str, destination: str,
                       studies_filter: Callable[[RootStudy], bool] = None,
                       files_filter: Callable[[File], bool] = None):
    project = find_project_by_name(project_name)
    if not project:
        logger.error(f"Project not found: {project_name}")
        return

    institute = find_institute_by_name(project.id, institute_name)

    logger.info(f"Institute name: {institute.name}, project type: {project.project_type_name}, "
                f"destination: {destination}")
    logger.debug(f"Institute id: {institute.id} and project id: {project.id}")

    studies = institute.studies

    if callable(studies_filter):
        studies = list(filter(studies_filter, studies))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for study in tqdm(studies, desc="Studies", unit='study'):
            study_folder = study.study_id_human_readable
            logger.debug(f"study folder: {study_folder}")
            study_destination = os.path.join(destination, institute.name, study_folder)

            files = study.files
            if callable(files_filter):
                files = list(filter(files_filter, files))

            total_size = sum([file.file_size for file in files if file.is_completed])
            fs = {executor.submit(file.download, study_destination, overwrite=False): file for file in files}
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


