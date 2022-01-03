# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from igtcloud.client.services.entities.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from igtcloud.client.services.entities.model.ai_suite_collection import AISuiteCollection
from igtcloud.client.services.entities.model.ai_suite_collection_all_of import AISuiteCollectionAllOf
from igtcloud.client.services.entities.model.ai_suite_connection import AISuiteConnection
from igtcloud.client.services.entities.model.ai_suite_project import AISuiteProject
from igtcloud.client.services.entities.model.ai_suite_project_all_of import AISuiteProjectAllOf
from igtcloud.client.services.entities.model.ai_suite_provider import AISuiteProvider
from igtcloud.client.services.entities.model.ai_suite_provider_all_of import AISuiteProviderAllOf
from igtcloud.client.services.entities.model.ai_suite_resource import AISuiteResource
from igtcloud.client.services.entities.model.account_status_model import AccountStatusModel
from igtcloud.client.services.entities.model.annotation_state_model import AnnotationStateModel
from igtcloud.client.services.entities.model.config_model import ConfigModel
from igtcloud.client.services.entities.model.contact_model import ContactModel
from igtcloud.client.services.entities.model.credentials_model import CredentialsModel
from igtcloud.client.services.entities.model.details_model import DetailsModel
from igtcloud.client.services.entities.model.electronic_record_state_model import ElectronicRecordStateModel
from igtcloud.client.services.entities.model.entry_model import EntryModel
from igtcloud.client.services.entities.model.file_model import FileModel
from igtcloud.client.services.entities.model.file_size_model import FileSizeModel
from igtcloud.client.services.entities.model.file_sizes_model import FileSizesModel
from igtcloud.client.services.entities.model.files_response import FilesResponse
from igtcloud.client.services.entities.model.group_model import GroupModel
from igtcloud.client.services.entities.model.groups_models import GroupsModels
from igtcloud.client.services.entities.model.hospital_create_model import HospitalCreateModel
from igtcloud.client.services.entities.model.hospital_model import HospitalModel
from igtcloud.client.services.entities.model.hospital_response import HospitalResponse
from igtcloud.client.services.entities.model.hospitals_response import HospitalsResponse
from igtcloud.client.services.entities.model.issue_model import IssueModel
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.organization_role_model import OrganizationRoleModel
from igtcloud.client.services.entities.model.profile_model import ProfileModel
from igtcloud.client.services.entities.model.project_create_model import ProjectCreateModel
from igtcloud.client.services.entities.model.project_model import ProjectModel
from igtcloud.client.services.entities.model.project_response import ProjectResponse
from igtcloud.client.services.entities.model.projects_response import ProjectsResponse
from igtcloud.client.services.entities.model.series_create_model import SeriesCreateModel
from igtcloud.client.services.entities.model.service_create_model import ServiceCreateModel
from igtcloud.client.services.entities.model.service_create_response import ServiceCreateResponse
from igtcloud.client.services.entities.model.service_model import ServiceModel
from igtcloud.client.services.entities.model.storage_model import StorageModel
from igtcloud.client.services.entities.model.task_completed_model import TaskCompletedModel
from igtcloud.client.services.entities.model.user_activation_create_model import UserActivationCreateModel
from igtcloud.client.services.entities.model.user_activation_model import UserActivationModel
from igtcloud.client.services.entities.model.user_create_model import UserCreateModel
from igtcloud.client.services.entities.model.user_info_model import UserInfoModel
from igtcloud.client.services.entities.model.user_settings_model import UserSettingsModel
from igtcloud.client.services.entities.model.users_groups_model import UsersGroupsModel
from igtcloud.client.services.entities.model.users_groups_models import UsersGroupsModels
