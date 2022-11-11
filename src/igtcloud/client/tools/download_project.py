import logging
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable

from tqdm.auto import tqdm

from igtcloud.client.tools.common import find_project_by_name
from ..services.entities.model.file import File

logger = logging.getLogger(__name__)


def download_project(
        project_name: str,
        destination: str,
        files_filter: Callable[[File], bool] = None,
        include_modified_date=False
):
    project = find_project_by_name(project_name)

    if not project:
        logger.error(f"Project not found: {project_name}")

        return

    fs = dict()
    files = list(filter(files_filter, project.files))
    total_size = sum([file.file_size for file in files if file.is_completed])
    destination = os.path.join(destination, 'files')

    with ThreadPoolExecutor(max_workers=4) as executor:
        for file in files:
            future = executor.submit(
                file.download,
                destination,
                overwrite=False,
                include_modified_date=include_modified_date
            )
            fs[future] = file

        with tqdm(total=total_size, desc="Project files", unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            for future in as_completed(fs):
                file = fs.pop(future)

                pbar.update(file.file_size)

                try:
                    if future.result():
                        logger.debug(f"Downloaded: {file.file_name}")
                    else:
                        logger.debug(f"Skipped: {file.file_name}")
                except Exception:
                    logger.exception(f"Exception during download of {file.file_name}")
