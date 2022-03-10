import os

from .base_service import BaseService


def _setup_service(module):
    def _api_key_hook(conf: module.Configuration):
        auth_handler = conf.auth_handler_provider()
        conf.api_key['jwt'] = auth_handler.jwt_token
        conf.api_key['csrf_token'] = auth_handler.csrf_token

    config = module.Configuration(api_key=dict(jwt=None, csrf_token=None))
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
    from .entities_service import EntitiesService, _patch_service
    client = _setup_service(entities)
    service = EntitiesService(client)
    _patch_service(service)

    return service


def _setup_auth():
    from . import auth
    from .auth_service import AuthService, _patch_service
    client = _setup_service(auth)
    service = AuthService(client)
    _patch_service(service)

    return service


def _setup_action():
    from . import action
    from .action_service import ActionService, _patch_service
    client = _setup_service(action)
    service = ActionService(client)
    _patch_service(service)

    return service


def set_auth(auth):
    auth_service.auth_handler = auth
    action_service.auth_handler = auth
    entities_service.auth_handler = auth


auth_service = _setup_auth()
action_service = _setup_action()
entities_service = _setup_entities()

__all__ = ['auth_service', 'entities_service', 'action_service', 'set_auth']
