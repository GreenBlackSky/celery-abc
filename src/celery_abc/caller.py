from abc import ABCMeta
from types import MethodType


class CallerMetaBase(ABCMeta):

    def _init_overriden(self, celery):
        self._celery = celery

    class _CalledTask:
        def __init__(self, name):
            self._name = name

        def __call__(self, obj, *kargs):
            # get args names
            print("Sending", self._name, obj._celery, kargs)

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return MethodType(self, obj)

    def __new__(cls, name, bases, dct):
        dct['__init__'] = CallerMetaBase._init_overriden
        for attr_name in dir(bases[0]):
            if not attr_name.startswith('__'):
                dct[attr_name] = CallerMetaBase._CalledTask(attr_name)

        return ABCMeta.__new__(cls, name, bases, dct)
