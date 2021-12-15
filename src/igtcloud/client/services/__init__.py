import os

from igtcloud.client.core.auth import AuthHandler

auth_handler = AuthHandler()


def _setup_service(module):
    def _api_key_hook(conf: module.Configuration):
        conf.api_key['jwt'] = auth_handler.token
        conf.api_key['csrf'] = auth_handler.csrf_token

    config = module.Configuration(host=f"{auth_handler.domain}/api/data", api_key=dict(jwt=None, csrf=None))
    config.refresh_api_key_hook = _api_key_hook
    config.discard_unknown_keys = True
    for p in 'https_proxy', 'HTTPS_PROXY', 'http_proxy', 'HTTP_PROXY':
        if p in os.environ:
            config.proxy = os.environ[p]
            config.no_proxy = os.environ.get('no_proxy', os.environ.get('NO_PROXY', None))
            break
    api_client = module.ApiClient(configuration=config)
    return api_client


def _setup_entities():
    from . import entities
    from .entities.apis import (ProjectsApi, HospitalsApi, IntegrationsApi)
    client = _setup_service(entities)

    class EntitiesService(ProjectsApi, HospitalsApi, IntegrationsApi):
        def __init__(self, api_client):
            ProjectsApi.__init__(self, api_client)
            HospitalsApi.__init__(self, api_client)
            IntegrationsApi.__init__(self, api_client)

    return EntitiesService(client)


entities_service = _setup_entities()

__all__ = ['entities_service']
