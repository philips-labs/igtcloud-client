import datetime
import io
import os
from typing import Optional, Iterable, Callable, Any

import boto3
import dateutil.parser

from .auth.model.credentials import Credentials
from .base_service import BaseService, CollectionWrapper
from .entities.apis import (ProjectsApi, InstitutesApi, IntegrationsApi, UsersApi, OrganizationsApi)
from .entities.model.file import File
from .entities.model.institute import Institute
from .entities.model.project import Project
from .entities.model.root_study import RootStudy
from .entities.model.series import Series


class EntitiesService(BaseService, ProjectsApi, InstitutesApi, IntegrationsApi, UsersApi, OrganizationsApi):
    def __init__(self, api_client):
        BaseService.__init__(self, api_client, '/api/data')
        ProjectsApi.__init__(self, api_client)
        InstitutesApi.__init__(self, api_client)
        IntegrationsApi.__init__(self, api_client)
        UsersApi.__init__(self, api_client)
        OrganizationsApi.__init__(self, api_client)


class FilesCollectionWrapper(CollectionWrapper):
    def __init__(self, s3_prefix: str, iterable: Iterable[File] = None, f_init: Callable[[], Iterable[File]] = None,
                 f_extend: Callable[[Iterable[File]], Iterable[File]] = None, f_remove: Callable[[File], None] = None,
                 f_auth: Callable[[str, str], Optional[Credentials]] = None,
                 f_callback: Callable[[File], Any] = None) -> None:
        self.s3_prefix = s3_prefix
        if not self.s3_prefix.endswith('/'):
            self.s3_prefix += '/'
        f_add = None
        if callable(f_extend):
            f_add = self._add
        self._extend = f_extend
        self._auth = f_auth
        self._callback = f_callback
        self._credentials = dict()
        super().__init__(iterable, f_init, f_add, f_remove)
        self._add_wrapper()

    def __contains__(self, o: object) -> bool:
        if not isinstance(o, File):
            return False

        return any(item.key == o.key for item in self)

    def index(self, __value: File, *args, **kwargs) -> int:
        if isinstance(__value, File):
            for ix, item in enumerate(self):
                if item.key == __value.key:
                    return ix
        raise ValueError(f"{__value} not in list")

    def _add(self, obj: File) -> Optional[File]:
        if obj not in self:
            objs = self._extend([obj])
            self._add_wrapper(objs)
            return objs[0]
        return None

    def _add_wrapper(self, collection: Iterable[File] = None):
        if collection is None:
            collection = self
        for file in collection:
            file._creds_wrapper = lambda action: FilesCollectionWrapper.get_credentials(self, action)

    def extend(self, __iterable: Iterable[File]) -> None:
        if callable(self._extend):
            objs = self._extend([obj for obj in __iterable if obj not in self])
            self._add_wrapper(objs)
            list.extend(self, objs)
        else:
            raise RuntimeError("Not supported")

    def get_credentials(self, action):
        if action not in self._credentials or (dateutil.parser.parse(self._credentials[action].expires)
                                               - datetime.datetime.now()).total_seconds() < 3600:
            if not callable(self._auth):
                raise RuntimeError("No method for retrieving credentials")
            self._credentials[action] = self._auth(action, self.s3_prefix)
        return self._credentials.get(action)

    def upload(self, filename: str, key: str = None):
        abs_path = os.path.abspath(filename)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"File {filename} not found")

        if key is None:
            key = os.path.basename(abs_path)

        key = self.s3_prefix + key
        file = File(key=key, file_size=os.path.getsize(abs_path))
        self.append(file)
        try:
            file = self[self.index(file)]
        except Exception:
            pass  # Ignore index exceptions
        bucket = get_s3_bucket(file, 'PUT')
        extra_args = {'ServerSideEncryption': 'AES256'}
        bucket.upload_file(Filename=abs_path, Key=file.key, ExtraArgs=extra_args)
        file.is_completed = True
        file.is_new = False
        file.progress_in_bytes = file.file_size
        file.progress_percentage = 100
        file.type = os.path.splitext(abs_path)[1]
        file.file_name = key[len(self.s3_prefix):]
        if callable(self._callback):
            self._callback(file)


def _patch_service(service: EntitiesService):
    Project.institutes = property(lambda project: get_project_institutes(service, project), no_setter)
    Project.files = property(lambda project: get_project_files(service, project), no_setter)
    Institute.studies = property(lambda institute: get_institute_studies(service, institute), no_setter)
    study_series = property(lambda study: get_study_series(service, study), no_setter)
    study_files = property(lambda study: get_study_files(service, study), no_setter)
    study_dicom = property(lambda study: get_dicom_files(service, study), no_setter)
    for discriminator in RootStudy.discriminator.values():
        for study_class in discriminator.values():
            study_class.series = study_series
            study_class.files = study_files
            study_class.dicom = study_dicom


    File.required_properties.add('_creds_wrapper')
    File._creds_wrapper = None
    File.credentials = lambda file, action: get_file_creds(file, action)
    File.download = lambda file, destination: download_file(file, destination)
    File.download_fileobj = lambda file, file_obj: download_fileobj(file, file_obj)


def no_setter(self, value):
    raise RuntimeError("Not supported")


def get_project_institutes(service: EntitiesService, project: Project) -> CollectionWrapper[Institute]:
    data_store = project.get('_data_store')
    initial_value = data_store.get('institutes', None)
    if not isinstance(initial_value, CollectionWrapper):
        data_store['institutes'] = CollectionWrapper(iterable=initial_value,
                                                     f_init=lambda: service.get_institutes(project.id),
                                                     f_add=lambda x: service.post_institutes(project.id, x))
    return data_store['institutes']


def get_institute_studies(service: EntitiesService, institute: Institute) -> CollectionWrapper[RootStudy]:
    data_store = institute.get('_data_store')
    initial_value = data_store.get('studies', None)
    if not isinstance(initial_value, CollectionWrapper):
        data_store['studies'] = CollectionWrapper(iterable=initial_value,
                                                  f_init=lambda: service.get_studies(institute.id),
                                                  f_add=lambda x: service.post_studies(institute.id, x),
                                                  f_remove=lambda x: service.delete_study(institute.id,
                                                                                          x.study_database_id))
    return data_store['studies']


def get_study_series(service: EntitiesService, study: RootStudy) -> CollectionWrapper[Series]:
    data_store = study.get('_data_store')
    initial_value = data_store.get('series', None)
    if not isinstance(initial_value, CollectionWrapper):
        data_store['series'] = CollectionWrapper(iterable=initial_value,
                                                 f_init=lambda: service.get_study_series_list(study.institute_id,
                                                                                              study.study_database_id),
                                                 f_add=lambda x: service.put_study_series(study.institute_id,
                                                                                          study.study_database_id,
                                                                                          x.series_database_id, x),
                                                 f_remove=lambda x: service.delete_study_series(study.institute_id,
                                                                                                study.study_database_id,
                                                                                                x.series_database_id))
    return data_store['series']


def get_study_files(service: EntitiesService, study: RootStudy) -> FilesCollectionWrapper:
    data_store = study.get('_data_store')
    initial_value = data_store.get('files', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['files'] = FilesCollectionWrapper(s3_prefix=study.s3_prefix + 'files/',
                                                     f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                     f_init=lambda: service.get_study_files(study.institute_id,
                                                                                            study.study_database_id).files,
                                                     f_extend=lambda x: service.post_study_files(study.institute_id,
                                                                                                 study.study_database_id,
                                                                                                 x).files,
                                                     f_remove=lambda x: service.delete_study_files(study.institute_id,
                                                                                                   study.study_database_id,
                                                                                                   keys=[x.key]),
                                                     f_callback=lambda x: process_file(study, x))
    return data_store['files']


def get_dicom_files(service: EntitiesService, study: RootStudy) -> FilesCollectionWrapper:
    data_store = study.get('_data_store')
    initial_value = data_store.get('dicom', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['dicom'] = FilesCollectionWrapper(s3_prefix=study.s3_prefix + '0/',
                                                     f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                     f_init=lambda: service.get_study_files(study.institute_id,
                                                                                            study.study_database_id,
                                                                                            auxiliary=True).dicom)
    return data_store['dicom']


def get_project_files(service: EntitiesService, project: Project) -> FilesCollectionWrapper:
    data_store = project.get('_data_store')
    initial_value = data_store.get('files', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['files'] = FilesCollectionWrapper(s3_prefix=project.s3_prefix,
                                                     f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                     f_init=lambda: service.get_project_files(project.id).files,
                                                     f_extend=lambda x: service.post_project_files(project.id, x).files,
                                                     f_remove=lambda x: service.delete_project_files(project.id,
                                                                                                     keys=[x.key]))
    return data_store['files']


def s3_creds(action: str, s3_prefix: str) -> Optional[Credentials]:
    from . import auth_service
    creds = auth_service.get_s3_credentials_resource(action, prefix=s3_prefix).policy_credentials
    if creds:
        return creds[0].credentials
    return None


def get_file_creds(file: File, action: str) -> Optional[Credentials]:
    creds_wrapper: Callable[[str], Optional[Credentials]] = file._creds_wrapper
    if callable(creds_wrapper):
        return creds_wrapper(action)
    else:
        return s3_creds(action, file.key)


def download_file(file: File, destination_dir: os.PathLike):
    bucket = get_s3_bucket(file, 'GET')
    destination = os.path.abspath(os.path.join(destination_dir, file.file_name))
    os.makedirs(os.path.abspath(destination_dir), exist_ok=True)
    bucket.download_file(Key=file.key, Filename=destination)


def download_fileobj(file: File, file_obj: io.IOBase):
    bucket = get_s3_bucket(file, 'GET')
    bucket.download_fileobj(Key=file.key, FileObj=file_obj)


def get_s3_bucket(file: File, action: str):
    creds = file.credentials(action)
    if not creds:
        raise RuntimeError("No valid credentials")
    creds_dict = dict(aws_access_key_id=creds.access_key,
                      aws_secret_access_key=creds.secret_key,
                      aws_session_token=creds.session_token)
    creds_dict = {k: v for k, v in creds_dict.items() if k}
    s3 = boto3.resource('s3', **creds_dict)
    return s3.Bucket(creds.bucket)


def process_file(study: RootStudy, file: File):
    if study.study_type in ['AnnotationStudy'] and file.type in ['.dcm', '.fxd', '']:
        from . import action_service
        from .action.model.preprocessing_request import PreprocessingRequest
        request = PreprocessingRequest(hospital_id=study.institute_id,
                                       study_id=study.study_database_id,
                                       patient_id=getattr(study, 'patient_database_id', None),
                                       uploaded_path=file.file_name)
        action_service.post_preprocess_file(request)