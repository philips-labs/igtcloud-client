import concurrent.futures
import json
import logging
import os.path
from getpass import getpass
from typing import Tuple, List

from tqdm.auto import tqdm

from igtcloud.client.services import entities_service
from igtcloud.client.services.base_service import CollectionWrapper
from igtcloud.client.services.entities.model.electronic_record_state import ElectronicRecordState
from igtcloud.client.services.entities.model.patient import Patient
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model_utils import validate_and_convert_types
from igtcloud.client.tools.common import find_project_and_institutes, study_key

logger = logging.getLogger(__name__)


def upload_project(local_folder: str, project_name: str, institute_name: str = None, submit: bool = False):
    project, institutes = find_project_and_institutes(project_name, institute_name)
    if not project:
        logger.error(f"Project not found: {project_name}")
        return

    if not institutes:
        logger.error(f"No institutes found")
        return

    _password = None
    if submit:
        _password = getpass("For electronic record state it is required to reenter the password")

    # Filter institutes to match local folders
    institutes = list(filter(lambda i: os.path.isdir(os.path.join(local_folder, i.name)), institutes))

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for institute in institutes:
            logger.info(f"Uploading to institute: {institute.name}")

            institute_dir = os.path.join(local_folder, institute.name)
            existing_studies = institute.studies

            local_study_folders = (os.path.join(institute_dir, d) for d in os.listdir(institute_dir) if
                                   os.path.isdir(os.path.join(institute_dir, d)))

            fs = [executor.submit(upload_study, project.study_type, study_folder, institute.id, existing_studies,
                                  _password) for study_folder in local_study_folders]

            for f in tqdm(concurrent.futures.as_completed(fs), total=len(fs), desc="Studies", unit='study'):
                study, files_uploaded, files_skipped = f.result()
                logger.info(f"Study: {study.study_id_human_readable} files_uploaded: {len(files_uploaded)}, "
                            f"files_skipped: {len(files_skipped)}")


def upload_study(study_type: str, study_folder: str, institute_id: str, studies: CollectionWrapper[RootStudy],
                 _submit_password: str = None) -> Tuple[RootStudy, List[str], List[str]]:
    local_study = None
    study_cls = entities_service.study_type_classes.get(study_type)
    study_json_file = os.path.join(study_folder, 'study.json')
    patient_name = os.path.basename(study_folder)
    if os.path.exists(study_json_file):
        try:
            with open(study_json_file, 'r') as f:
                data = json.load(f)
                data['studyType'] = study_type
            local_study = validate_and_convert_types(data,
                                                     (RootStudy,),
                                                     ['received_data'],
                                                     True,
                                                     True,
                                                     configuration=entities_service.api_client.configuration
                                                     )
        except Exception:
            logger.exception(f"Unable to parse {study_json_file}")
    if local_study is None:
        study_kwargs = dict(study_type=study_type, institute_id=institute_id)
        attr_candidates = ['name', 'clinical_study', 'subject_id']
        for attr in attr_candidates:
            if attr in study_cls.attribute_map:
                study_kwargs[attr] = patient_name
        if 'patient' in study_cls.attribute_map:
            study_kwargs['patient'] = Patient(patient_id=patient_name, patient_name=patient_name)
        local_study = study_cls(_spec_property_naming=True, **{study_cls.attribute_map[k]: v for
                                                               k, v in study_kwargs.items()})

    studies_lut = studies.to_dict(study_key)
    study = studies_lut.get(study_key(local_study), None)
    if not study:
        study = studies.append(local_study)

    if study is None:
        raise RuntimeError(f"Error creating study for {patient_name}")

    files_uploaded = list()
    files_skipped = list()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        fs = dict()
        with tqdm(total=0, leave=False, desc=f"Study {patient_name}", unit='B', unit_scale=True,
                  unit_divisor=1024) as pbar:
            def callback(x):
                pbar.update(x)

            if os.path.isdir(os.path.join(study_folder, 'files')) or os.path.isdir(os.path.join(study_folder, 'dicom')):
                # When directory contains files and/or dicom, only use files directory as study_root
                study_folder = os.path.join(study_folder, 'files')
            for root, dirs, local_files in os.walk(study_folder):
                for file in local_files:
                    file_path = os.path.join(root, file)
                    key = os.path.relpath(file_path, study_folder).replace(os.path.sep, '/')
                    size = os.path.getsize(file_path)
                    pbar.total += size
                    fs[executor.submit(study.files.upload, file_path, key, callback=callback)] = (key, size)
            for f in concurrent.futures.as_completed(fs.keys()):
                file, size = fs.pop(f)
                if f.result():
                    files_uploaded.append(file)
                else:
                    files_skipped.append(file)

    if _submit_password is not None:
        ers = ElectronicRecordState(username=entities_service.auth_handler.username, password=_submit_password,
                                    electronic_record_state='submitted')
        entities_service.post_study_electronic_record_state(institute_id, study.study_database_id, ers)

    return study, files_uploaded, files_skipped
