import os

from igtcloud.client.core.auth import AuthHandler


class BaseService:
    def __init__(self, api_client, host_path):
        self._host_path = host_path
        self.api_client = api_client
        self._auth_handler = None
        api_client.configuration.auth_handler_provider = self._get_auth_handler

    def _get_auth_handler(self):
        if self._auth_handler is None:
            self._auth_handler = AuthHandler()
        self.api_client.configuration.host = f"{self._auth_handler.domain}{self._host_path}"
        return self._auth_handler

    @property
    def auth_handler(self):
        return self._get_auth_handler()

    @auth_handler.setter
    def auth_handler(self, value):
        self._auth_handler = value


def _setup_service(module):
    def _api_key_hook(conf: module.Configuration):
        auth_handler = conf.auth_handler_provider()
        conf.api_key['jwt'] = auth_handler.jwt_token
        conf.api_key['csrf'] = auth_handler.csrf_token

    config = module.Configuration(api_key=dict(jwt=None, csrf=None))
    config.auth_handler_provider = None
    config.host = 'https://philips.com/test'
    config.refresh_api_key_hook = _api_key_hook
    config.discard_unknown_keys = True
    for p in 'https_proxy', 'HTTPS_PROXY', 'http_proxy', 'HTTP_PROXY':
        if p in os.environ:
            config.proxy = os.environ[p]
            config.no_proxy = os.environ.get('no_proxy', os.environ.get('NO_PROXY', None))
            break
    api_client = module.ApiClient(configuration=config)
    config.host = None
    return api_client


def _setup_entities():
    from . import entities
    from .entities.apis import (ProjectsApi, HospitalsApi)
    client = _setup_service(entities)

    class EntitiesService(BaseService, ProjectsApi, HospitalsApi):
        def __init__(self, api_client):
            BaseService.__init__(self, api_client, '/api/data')
            ProjectsApi.__init__(self, api_client)
            HospitalsApi.__init__(self, api_client)

    return EntitiesService(client)


def _setup_auth():
    from . import auth
    from .auth.apis import AuthApi
    client = _setup_service(auth)

    class AuthService(BaseService, AuthApi):
        def __init__(self, api_client):
            BaseService.__init__(self, api_client, '/api/auth')
            AuthApi.__init__(self, api_client)

    return AuthService(client)


entities_service = _setup_entities()
auth_service = _setup_auth()

__all__ = ['auth_service', 'entities_service']
