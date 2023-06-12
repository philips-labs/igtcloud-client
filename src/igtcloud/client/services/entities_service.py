import datetime
import io
import os
import uuid
from typing import Optional, Iterable, Callable, Any

import boto3
import dateutil.parser
from botocore.exceptions import HTTPClientError
from tenacity import retry, wait_exponential, retry_if_exception_type, stop_after_attempt

from .auth.model.credentials import Credentials
from .base_service import BaseService, CollectionWrapper
from .entities.apis import (ProjectsApi, InstitutesApi, IntegrationsApi, UsersApi, OrganizationsApi, ReportsApi)
from .entities.model.file import File
from .entities.model.institute import Institute
from .entities.model.project import Project
from .entities.model.root_study import RootStudy
from .entities.model.series import Series
from .utils.s3 import S3File


class EntitiesService(BaseService, ProjectsApi, InstitutesApi, IntegrationsApi, UsersApi, OrganizationsApi, ReportsApi):
    def __init__(self, api_client):
        BaseService.__init__(self, api_client, '/api/data')
        ProjectsApi.__init__(self, api_client)
        InstitutesApi.__init__(self, api_client)
        IntegrationsApi.__init__(self, api_client)
        UsersApi.__init__(self, api_client)
        OrganizationsApi.__init__(self, api_client)
        ReportsApi.__init__(self, api_client)

        self.study_type_classes = RootStudy.discriminator.get('study_type')
        self.series_type_classes = Series.discriminator.get('series_type')


class FilesCollectionWrapper(CollectionWrapper[File]):
    def __init__(self, s3_prefix: str, iterable: Iterable[File] = None, f_init: Callable[[], Iterable[File]] = None,
                 f_extend: Callable[[Iterable[File]], Iterable[File]] = None, f_remove: Callable[[File], None] = None,
                 f_auth: Callable[[str, str], Optional[Credentials]] = None,
                 f_callback: Callable[[File], Any] = None,
                 category: str = 'files') -> None:
        self.s3_prefix = s3_prefix
        self.category = category
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
            file._category = lambda: self.category

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

    def upload(self, filename: str, key: str = None, overwrite: bool = False,
               callback: Callable[[int], None] = None, trigger_action: bool = True) -> bool:
        abs_path = os.path.abspath(filename)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"File {filename} not found")

        if key is None:
            key = os.path.basename(abs_path)

        key = self.s3_prefix + key
        new_file = File(key=key, file_size=os.path.getsize(abs_path))
        if new_file not in self:
            file = self.append(new_file)
        else:
            file = self[self.index(new_file)]
            if file.file_size == new_file.file_size and file.is_completed and not overwrite:
                if callback:
                    callback(file.file_size)
                return False
        bucket = get_s3_bucket(file, 'PUT')
        extra_args = {'ServerSideEncryption': 'AES256'}
        kwargs = dict(Filename=abs_path, Key=file.key, ExtraArgs=extra_args)
        if callback:
            kwargs['Callback'] = callback
        bucket.upload_file(**kwargs)
        file.is_completed = True
        file.is_new = False
        file.progress_in_bytes = file.file_size
        file.progress_percentage = 100
        file.type = os.path.splitext(abs_path)[1]
        file.file_name = key[len(self.s3_prefix):]
        if callable(self._callback) and trigger_action:
            self._callback(file)
        return True


def _patch_service(service: EntitiesService):
    Project.institutes = property(lambda project: get_project_institutes(service, project), no_setter)
    Project.files = property(lambda project: get_project_files(service, project), no_setter)
    Institute.studies = property(lambda institute: get_institute_studies(service, institute), no_setter)
    Institute.dicom = property(get_institute_dicom, no_setter)
    study_series = property(lambda study: get_study_series(service, study), no_setter)
    study_files = property(lambda study: get_study_files(service, study), no_setter)
    study_dicom = property(lambda study: get_dicom_files(service, study), no_setter)
    study_annotations = property(lambda study: get_annotation_files(service, study), no_setter)
    for study_class in service.study_type_classes.values():
        study_class.series = study_series
        study_class.files = study_files
        study_class.dicom = study_dicom
        study_class.annotations = study_annotations

    File.required_properties.add('_creds_wrapper')
    File.required_properties.add('_category')
    File._creds_wrapper = None
    File._category = None
    File.credentials = get_file_creds
    File.download = download_file
    File.download_fileobj = download_fileobj
    File.open = open_file
    File.category = property(get_category)


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


def get_institute_dicom(institute: Institute) -> FilesCollectionWrapper:
    data_store = institute.get('_data_store')
    initial_value = data_store.get('dicom_uploads', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['dicom_uploads'] = FilesCollectionWrapper(s3_prefix=institute.s3_prefix + f"Import/{uuid.uuid4()}/",
                                                             f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                             f_extend=lambda x: x,
                                                             f_callback=lambda x: update_database(
                                                                 institute, x, institute.s3_prefix + "Import/"))
    return data_store['dicom_uploads']


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
                                                     category='files',
                                                     f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                     f_init=lambda: service.get_study_files(study.institute_id,
                                                                                            study.study_database_id).files,
                                                     f_extend=lambda x: service.post_study_files(study.institute_id,
                                                                                                 study.study_database_id,
                                                                                                 x).files,
                                                     f_remove=lambda x: service.delete_study_files(study.institute_id,
                                                                                                   study.study_database_id,
                                                                                                   keys=[x.key]),
                                                     f_callback=lambda x: file_upload_completed(study, x))
    return data_store['files']


def get_dicom_files(service: EntitiesService, study: RootStudy) -> FilesCollectionWrapper:
    data_store = study.get('_data_store')
    initial_value = data_store.get('dicom', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['dicom'] = FilesCollectionWrapper(s3_prefix=study.s3_prefix + '0/',
                                                     category='dicom',
                                                     f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                     f_init=lambda: get_aux_files(service, study, 'dicom'))
    return data_store['dicom']


def get_annotation_files(service: EntitiesService, study: RootStudy) -> FilesCollectionWrapper:
    data_store = study.get('_data_store')
    initial_value = data_store.get('annotations', None)
    if not isinstance(initial_value, FilesCollectionWrapper):
        data_store['annotations'] = FilesCollectionWrapper(s3_prefix=study.s3_prefix + 'annotations/',
                                                           category='annotations',
                                                           f_auth=lambda action, prefix: s3_creds(action, prefix),
                                                           f_init=lambda: get_aux_files(service, study, 'annotations'))
    return data_store['annotations']


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


@retry(stop=(stop_after_attempt(3)), wait=wait_exponential(),
       retry=retry_if_exception_type(HTTPClientError), reraise=True)
def download_file(file: File, destination_dir: os.PathLike, overwrite: bool = True,
                  callback: Callable[[int], None] = None, include_modified_date: bool = False):
    if not file.is_completed:
        return False
    destination = os.path.abspath(os.path.join(destination_dir, file.file_name))
    if os.path.exists(destination) and os.path.getsize(destination) == file.file_size and not overwrite:
        if callback:
            callback(file.file_size)
        return False
    bucket = get_s3_bucket(file, 'GET')
    os.makedirs(os.path.abspath(os.path.dirname(destination)), exist_ok=True)
    kwargs = dict(Key=file.key, Filename=destination)
    if callback:
        kwargs['Callback'] = callback
    bucket.download_file(**kwargs)

    if include_modified_date:
        metadata = get_s3_file_metadata(file, 'GET')
        epoch = metadata['LastModified'].timestamp()
        os.utime(destination, (epoch, epoch))

    return True


@retry(stop=(stop_after_attempt(3)), wait=wait_exponential(),
       retry=retry_if_exception_type(HTTPClientError), reraise=True)
def download_fileobj(file: File, file_obj: io.IOBase):
    bucket = get_s3_bucket(file, 'GET')
    bucket.download_fileobj(Key=file.key, Fileobj=file_obj)


def open_file(file: File, mode='rb', buffering=-1, **kwargs):
    if 'r' not in mode:
        raise RuntimeError("Mode should contain 'r'")
    binary = 'b' in mode
    bucket = get_s3_bucket(file, 'GET')
    s3_file = S3File(bucket.Object(file.key), mode=mode)
    if binary:
        if buffering == 0:
            return s3_file
        else:
            buffer_size = buffering if buffering > 0 else 10 * 1024 ** 2
            kwargs.setdefault('buffer_size', buffer_size)
            return io.BufferedReader(s3_file, **kwargs)
    else:
        return io.TextIOWrapper(s3_file, **kwargs)


def get_s3_bucket(file: File, action: str):
    creds = file.credentials(action)
    if not creds:
        raise RuntimeError("No valid credentials")
    creds_dict = dict(aws_access_key_id=creds.access_key,
                      aws_secret_access_key=creds.secret_key,
                      aws_session_token=creds.session_token)
    creds_dict = {k: v for k, v in creds_dict.items() if k}
    session = boto3.session.Session(**creds_dict)
    s3 = session.resource('s3')
    return s3.Bucket(creds.bucket)


def get_s3_file_metadata(file: File, action: str):
    creds = file.credentials(action)
    if not creds:
        raise RuntimeError("No valid credentials")
    creds_dict = dict(aws_access_key_id=creds.access_key,
                      aws_secret_access_key=creds.secret_key,
                      aws_session_token=creds.session_token)
    creds_dict = {k: v for k, v in creds_dict.items() if k}
    session = boto3.session.Session(**creds_dict)
    s3 = session.client('s3')

    return s3.head_object(Bucket=creds.bucket, Key=file.key)


def file_upload_completed(study: RootStudy, file: File):
    from . import entities_service
    from .entities.model.file_upload_completed import FileUploadCompleted
    request = FileUploadCompleted(uploaded_path=file.file_name, trigger_action=True)
    entities_service.post_study_files_upload_completed(payload=request,
                                                       hospital_id=study.institute_id,
                                                       study_id=study.study_database_id)


def update_database(institute: Institute, file: File, common_prefix: str):
    from . import action_service
    from .action.model.update_database_request import UpdateDatabaseRequest
    request = UpdateDatabaseRequest(hospital_id=institute.id,
                                    uploaded_path=file.key.replace(common_prefix, ""),
                                    is_prefix=True)
    action_service.post_update_database(request)


def get_category(file: File) -> str:
    if callable(file._category):
        return file._category()
    return 'files'


def get_aux_files(service: EntitiesService, study: RootStudy, aux: str):
    files = service.get_study_files(study.institute_id, study.study_database_id, auxiliary=True)
    return getattr(files, aux, [])
