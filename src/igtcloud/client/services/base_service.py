from typing import Iterable, TypeVar, SupportsIndex, Callable, Generic, List, Dict

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


_T = TypeVar("_T")
_KT = TypeVar("_KT")


class CollectionWrapper(list, Generic[_T]):
    def __init__(self, iterable: Iterable[_T] = None,
                 f_init: Callable[[], Iterable[_T]] = None,
                 f_add: Callable[[_T], _T] = None,
                 f_remove: Callable[[_T], None] = None) -> None:
        self._init = f_init
        self._add = f_add
        self._remove = f_remove
        if iterable:
            super().__init__(iterable)
        else:
            if callable(self._init):
                super().__init__(self._init())
            else:
                super().__init__()

    def clear(self) -> None:
        raise RuntimeError("Not supported")

    def copy(self) -> List[_T]:
        return super().copy()

    def append(self, __object: _T) -> _T:
        if callable(self._add):
            obj = self._add(__object)
            if obj is not None:
                super().append(obj)
                return obj
        else:
            raise RuntimeError("Not supported")

    def extend(self, __iterable: Iterable[_T]) -> None:
        if callable(self._add):
            for __object in __iterable:
                obj = self._add(__object)
                super().append(obj)
        else:
            raise RuntimeError("Not supported")

    def pop(self, __index: SupportsIndex = ...) -> _T:
        raise RuntimeError("Not supported")

    def insert(self, __index: SupportsIndex, __object: _T) -> None:
        if callable(self._add):
            obj = self._add(__object)
            super().insert(__index, obj)
        else:
            raise RuntimeError("Not supported")

    def remove(self, __value: _T) -> None:
        if callable(self._remove):
            self._remove(__value)
            super().remove(__value)
        else:
            raise RuntimeError("Not supported")

    def reload(self) -> None:
        if callable(self._init):
            super().clear()
            super().extend(self._init())

    def to_dict(self, key_fn: Callable[[_T], _KT]) -> Dict[_KT, _T]:
        return {key_fn(item): item for item in self.copy()}

