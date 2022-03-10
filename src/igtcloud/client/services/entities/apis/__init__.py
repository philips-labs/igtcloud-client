
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.applications_api import ApplicationsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from igtcloud.client.services.entities.api.applications_api import ApplicationsApi
from igtcloud.client.services.entities.api.institutes_api import InstitutesApi
from igtcloud.client.services.entities.api.integrations_api import IntegrationsApi
from igtcloud.client.services.entities.api.organizations_api import OrganizationsApi
from igtcloud.client.services.entities.api.projects_api import ProjectsApi
from igtcloud.client.services.entities.api.tasks_api import TasksApi
from igtcloud.client.services.entities.api.users_api import UsersApi
