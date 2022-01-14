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
from igtcloud.client.services.entities.model.account_status import AccountStatus
from igtcloud.client.services.entities.model.annotation_series import AnnotationSeries
from igtcloud.client.services.entities.model.annotation_series_all_of import AnnotationSeriesAllOf
from igtcloud.client.services.entities.model.annotation_state import AnnotationState
from igtcloud.client.services.entities.model.annotation_study import AnnotationStudy
from igtcloud.client.services.entities.model.annotation_study_all_of import AnnotationStudyAllOf
from igtcloud.client.services.entities.model.application import Application
from igtcloud.client.services.entities.model.base_study import BaseStudy
from igtcloud.client.services.entities.model.base_study_all_of import BaseStudyAllOf
from igtcloud.client.services.entities.model.contact import Contact
from igtcloud.client.services.entities.model.core_labs_series import CoreLabsSeries
from igtcloud.client.services.entities.model.core_labs_series_all_of import CoreLabsSeriesAllOf
from igtcloud.client.services.entities.model.core_labs_study import CoreLabsStudy
from igtcloud.client.services.entities.model.core_labs_study_all_of import CoreLabsStudyAllOf
from igtcloud.client.services.entities.model.echo_nav_series import EchoNavSeries
from igtcloud.client.services.entities.model.echo_nav_series_all_of import EchoNavSeriesAllOf
from igtcloud.client.services.entities.model.echo_nav_study import EchoNavStudy
from igtcloud.client.services.entities.model.echo_nav_study_all_of import EchoNavStudyAllOf
from igtcloud.client.services.entities.model.electronic_record_state import ElectronicRecordState
from igtcloud.client.services.entities.model.epd_study import EpdStudy
from igtcloud.client.services.entities.model.epd_study_all_of import EpdStudyAllOf
from igtcloud.client.services.entities.model.epd_study_event import EpdStudyEvent
from igtcloud.client.services.entities.model.file import File
from igtcloud.client.services.entities.model.file_sizes import FileSizes
from igtcloud.client.services.entities.model.files import Files
from igtcloud.client.services.entities.model.group import Group
from igtcloud.client.services.entities.model.hsdp_details import HsdpDetails
from igtcloud.client.services.entities.model.hsdp_issue import HsdpIssue
from igtcloud.client.services.entities.model.hsdp_response import HsdpResponse
from igtcloud.client.services.entities.model.i_guide_u_study import IGuideUStudy
from igtcloud.client.services.entities.model.i_guide_u_study_all_of import IGuideUStudyAllOf
from igtcloud.client.services.entities.model.igt_cloud_series import IgtCloudSeries
from igtcloud.client.services.entities.model.igt_cloud_series_all_of import IgtCloudSeriesAllOf
from igtcloud.client.services.entities.model.institute import Institute
from igtcloud.client.services.entities.model.marvel_series import MarvelSeries
from igtcloud.client.services.entities.model.marvel_series_all_of import MarvelSeriesAllOf
from igtcloud.client.services.entities.model.marvel_study import MarvelStudy
from igtcloud.client.services.entities.model.marvel_study_all_of import MarvelStudyAllOf
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage
from igtcloud.client.services.entities.model.organization_role import OrganizationRole
from igtcloud.client.services.entities.model.patient import Patient
from igtcloud.client.services.entities.model.profile import Profile
from igtcloud.client.services.entities.model.project import Project
from igtcloud.client.services.entities.model.root_study import RootStudy
from igtcloud.client.services.entities.model.series import Series
from igtcloud.client.services.entities.model.service import Service
from igtcloud.client.services.entities.model.storage import Storage
from igtcloud.client.services.entities.model.storage_config import StorageConfig
from igtcloud.client.services.entities.model.storage_credentials import StorageCredentials
from igtcloud.client.services.entities.model.study import Study
from igtcloud.client.services.entities.model.task_completed import TaskCompleted
from igtcloud.client.services.entities.model.training_application import TrainingApplication
from igtcloud.client.services.entities.model.user import User
from igtcloud.client.services.entities.model.user_activation_request import UserActivationRequest
from igtcloud.client.services.entities.model.user_request import UserRequest
from igtcloud.client.services.entities.model.user_settings import UserSettings
from igtcloud.client.services.entities.model.users_groups import UsersGroups
from igtcloud.client.services.entities.model.we_trust_series import WeTrustSeries
from igtcloud.client.services.entities.model.we_trust_series_all_of import WeTrustSeriesAllOf
from igtcloud.client.services.entities.model.we_trust_study import WeTrustStudy
from igtcloud.client.services.entities.model.we_trust_study_all_of import WeTrustStudyAllOf
