from abc import ABCMeta
from functools import partial


class RecieverMetaBase(ABCMeta):

    class _HUB:
        pass

    def _init_overriden(self, celery):
        # register tasks
        self._celery = celery

    def __new__(cls, name, bases, dct):
        hub = RecieverMetaBase._HUB()
        dct['__init__'] = RecieverMetaBase._init_overriden
        for attr_name, method in dct.items():
            if not attr_name.startswith('__'):
                method = partial(method, hub)
                setattr(hub, attr_name, method)
                dct[attr_name] = method
        return ABCMeta.__new__(cls, name, bases, dct)
