import logging
import logging
import os
from csv import DictWriter, DictReader
from typing import Optional, Callable

from igtcloud.client.services.entities.model.file import File
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model_utils import model_to_dict
from igtcloud.client.tools.common import flatten_dict, \
    find_project_and_institutes

logger = logging.getLogger(__name__)


def list_project(project_name: str, destination: str, institute_name: Optional[str] = None,
                 list_files: bool = False, studies_filter: Callable[[RootStudy], bool] = None,
                 files_filter: Callable[[File], bool] = None):
    project, institutes = find_project_and_institutes(project_name, institute_name)
    if not project:
        logger.error(f"Project not found: {project_name}")
        return

    if not institutes:
        logger.error(f"No institutes found")
        return

    exclude_fields = ['studyType', 's3Prefix', 'patientS3Prefix']
    file_fields = ['filename', 'filesize']

    csv_filename = f'cloud_{institutes[0].id}.csv' if institute_name else f'cloud_{project.name}.csv'
    csv_filename = os.path.join(destination, csv_filename)
    mode = 'a' if os.path.exists(csv_filename) else 'w'
    with open(csv_filename, mode, newline='\n') as f:
        csv = None

        for institute in institutes:
            logger.info(f"Institute name: {institute.name}, project type: {project.project_type_name}, "
                        f"csv: {csv_filename}")
            logger.debug(f"Institute id: {institute.id} and project id: {project.id}")

            studies = institute.studies

            if callable(studies_filter):
                studies = list(filter(studies_filter, studies))

            if not studies:
                continue

            for study in studies:
                csv_data = flatten_dict(model_to_dict(study, serialize=True))
                if csv is None:
                    if mode == 'a':
                        with open(csv_filename, 'r') as f2:
                            csv = DictReader(f2)
                            fieldnames = csv.fieldnames
                    else:
                        fieldnames = [field for field in csv_data.keys() if field not in exclude_fields]
                        if list_files:
                            fieldnames.extend(file_fields)
                    csv = DictWriter(f, fieldnames, extrasaction='ignore')
                    if mode == 'w':
                        csv.writeheader()
                if list_files:
                    files = study.files
                    if callable(files_filter):
                        files = list(filter(files_filter, files))
                    for file in files:
                        csv_data['filename'] = file.file_name
                        csv_data['filesize'] = file.file_size
                        csv.writerow(csv_data)

                if 'filename' not in csv_data:  # Also write row if list_files AND no files
                    csv.writerow(csv_data)
