import concurrent.futures
import json
import logging
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed
from getpass import getpass
from typing import Tuple, List

from igtcloud.client.services.entities.model.project import Project
from tqdm.auto import tqdm

from igtcloud.client.services import entities_service
from igtcloud.client.services.base_service import CollectionWrapper
from igtcloud.client.services.entities.model.electronic_record_state import ElectronicRecordState
from igtcloud.client.services.entities.model.patient import Patient
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model_utils import validate_and_convert_types
from igtcloud.client.tools.common import find_project_and_institutes, study_key

logger = logging.getLogger(__name__)


def upload_project(local_folder: str, project_name: str, institute_name: str = None, submit: bool = False,
                   max_workers_studies: int = None, max_workers_files: int = None, folder_structure: str = None,
                   category: str = None):
    project, institutes = find_project_and_institutes(project_name, institute_name)

    if not project and not institutes:
        logger.error("No project and institutes found")
        return

    _password = None
    if submit:
        _password = getpass("For electronic record state it is required to reenter the password")

    if category.lower() == "annotations":
        return upload_annotation_files_private_method(institutes, local_folder, max_workers_files)

    if project:
        # Project level file upload when there is a "files" folder in the root directory
        files_folder = os.path.join(local_folder, 'files')

        upload_project_files(project, files_folder, max_workers_files)

    # Filter institutes to match local folders
    institutes = list(filter(lambda i: os.path.isdir(os.path.join(local_folder, i.name)), institutes))

    if not institutes:
        logger.info("No institute folders found to upload. Skipping...")

        return

    if folder_structure not in ['flat', 'hierarchical']:
        folder_structure = 'flat'

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers_studies or 4) as executor:
        for institute in institutes:
            logger.info(f"Uploading to institute: {institute.name}")

            institute_dir = os.path.join(local_folder, institute.name)
            existing_studies = institute.studies

            local_studies = {}

            for d in os.listdir(institute_dir):
                if os.path.isdir(os.path.join(institute_dir, d)):
                    if folder_structure == 'flat':
                        study_dir = os.path.join(institute_dir, d)
                        patient_name = os.path.basename(study_dir)

                        local_studies[study_dir] = patient_name
                    else:
                        patient_dir = os.path.join(institute_dir, d)
                        patient_name = os.path.basename(patient_dir)

                        for study_dir in os.listdir(patient_dir):
                            study_dir = os.path.join(patient_dir, study_dir)

                            local_studies[study_dir] = patient_name

            fs = [executor.submit(upload_study, institute.study_type, study_folder, local_studies[study_folder],
                                  institute.id, existing_studies, _password, max_workers_files) for study_folder in local_studies]

            for f in tqdm(concurrent.futures.as_completed(fs), total=len(fs), desc="Studies", unit='study'):
                study, files_uploaded, files_skipped = f.result()
                logger.info(f"Study: {study.study_id_human_readable} files_uploaded: {len(files_uploaded)}, "
                            f"files_skipped: {len(files_skipped)}")


def upload_annotation_files_private_method(institutes, local_folder, max_workers_files):
    # Annotation file upload
    logger.info("Annotation File Uploading...")
    annotation_files = []
    if os.path.isdir(local_folder):
        for root, dirs, local_files in os.walk(local_folder):
            local_path = root
            annotation_files.extend(local_files)
    else:
        logger.error("Not a valid Directory")
    initial_path = local_path.split("/")
    annotation_paths = local_path.split("/0") if "/0" in local_path else local_path.split("/files")
    annotation_path = annotation_paths[1]
    annotation_path = "0" + annotation_path if "/0" in local_path else "files" + annotation_path
    if "---" in initial_path[2]:
        study_id_human_readable = initial_path[2].replace("---", "/")
    else:
        study_id_human_readable = initial_path[2] + "/" + initial_path[3]
    for institute in institutes:
        for studies in institute.studies:
            if studies.study_id_human_readable == study_id_human_readable:
                s3_prefix_for_annotation_file = studies.s3_prefix
                hospital_id = studies.hospital_id
                study_id = studies.study_database_id
                break

    studies_id = entities_service.get_study(hospital_id=hospital_id, study_id=study_id)

    files_uploaded = list()
    files_skipped = list()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers_files or 4) as executor:
        fs = dict()
        with tqdm(total=0, leave=False, desc=f" Annotation file Upload", unit='B', unit_scale=True,
                  unit_divisor=1024) as pbar:
            def callback(x):
                pbar.update(x)

            for annotation_file in annotation_files:
                if annotation_file.endswith(".json"):
                    try:
                        local_path_json = local_path.replace("/name", "")
                        annotation_path_json = annotation_path.replace("/name", "")
                        file_path = local_path_json + "/" + annotation_file
                        size = os.path.getsize(file_path)
                        pbar.total += size
                        with open(os.path.abspath(file_path), "r") as file:
                            json.loads(file.read())
                    except ValueError as e:
                        logger.error("Annotation File JSON is not valid : %s" % e)
                        return
                    fs[executor.submit(studies_id.annotations.upload, file_path,
                                       annotation_path_json + "/" + annotation_file, callback=callback)] = (
                    s3_prefix_for_annotation_file, size)
                else:
                    file_path = local_path + "/" + annotation_file
                    size = os.path.getsize(file_path)
                    pbar.total += size
                    fs[executor.submit(studies_id.annotations.upload, file_path,
                                       annotation_path + "/" + annotation_file, callback=callback)] = (
                    s3_prefix_for_annotation_file, size)

            for f in concurrent.futures.as_completed(fs.keys()):
                file, size = fs.pop(f)
                if f.result():
                    files_uploaded.append(file)
                else:
                    files_skipped.append(file)
    logger.info(f"files_uploaded: {len(files_uploaded)}, "
                                f"files_skipped: {len(files_skipped)}")
    logger.info("Annotation File uploaded successfully")
    return


def upload_study(study_type: str, study_folder: str, patient_name: str, institute_id: str,
                 studies: CollectionWrapper[RootStudy], _submit_password: str = None,
                 max_workers_files: int = None) -> Tuple[RootStudy, List[str], List[str]]:
    local_study = None
    study_cls = entities_service.study_type_classes.get(study_type)
    study_json_file = os.path.join(study_folder, 'study.json')

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

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers_files or 4) as executor:
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


def upload_project_files(project: Project, files_folder: str, max_workers_files: int):
    if not os.path.isdir(files_folder):
        logger.info("'files' is not a directory. Skipping project files upload...")

        return

    if not os.listdir(files_folder):
        logger.info("No project files to upload. Skipping...")

        return

    fs = dict()
    files_uploaded = list()
    files_skipped = list()

    with ThreadPoolExecutor(max_workers=max_workers_files or 4) as executor:
        with tqdm(total=0, desc="Project files", unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            for root, _, files in os.walk(files_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    size = os.path.getsize(file_path)
                    key = os.path.relpath(file_path, files_folder).replace(os.path.sep, '/')
                    pbar.total += size
                    future = executor.submit(project.files.upload, file_path, key, callback=pbar.update)
                    fs[future] = (file, size)

            for f in as_completed(fs.keys()):
                file, size = fs.pop(f)

                if f.result():
                    files_uploaded.append(file)
                else:
                    files_skipped.append(file)

    upload_count = len(files_uploaded)
    skip_count = len(files_skipped)

    logger.info(f"Project: {project.get('name')} files_uploaded: {upload_count}, files_skipped: {skip_count}")