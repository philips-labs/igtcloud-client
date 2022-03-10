from .base_service import BaseService
from .auth.apis import AuthApi


class AuthService(BaseService, AuthApi):
    def __init__(self, api_client):
        BaseService.__init__(self, api_client, '/api/auth')
        AuthApi.__init__(self, api_client)


def _patch_service(service: AuthService):
    pass
