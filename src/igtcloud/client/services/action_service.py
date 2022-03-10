from . import BaseService
from .action.apis import ActionApi


class ActionService(BaseService, ActionApi):
    def __init__(self, api_client):
        BaseService.__init__(self, api_client, '/api/action')
        ActionApi.__init__(self, api_client)


def _patch_service(service: ActionService):
    pass
