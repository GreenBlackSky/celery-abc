"""Replace abstract interface methods with calls of `celery` tasks."""

from abc import ABCMeta
from inspect import FullArgSpec, getfullargspec
from types import MethodType


class CallerMetaBase(ABCMeta):
    """
    Metabase class for your interface on caller's side.

    It replaces abstract methods with `celery` calls with names like
    `Interface.method`.
    """

    def _init_overriden(self, celery):
        self._celery = celery

    class _CalledTask:
        def __init__(self, name, args_info: FullArgSpec):
            self._name = name
            self._arg_names = [arg for arg in args_info.args if arg != 'self']
            self._defaults = args_info.defaults

        def __call__(self, obj, *args, **kargs):
            all_args = {name: val for name, val in zip(self._arg_names, args)}
            all_args.update(kargs)
            return obj._celery.send_task(self._name, kwargs=all_args).get()

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return MethodType(self, obj)

    def __new__(cls, name, bases, dct):
        """Create new class with all public methods replaced with rpc calls."""
        dct['__init__'] = CallerMetaBase._init_overriden
        base_name = bases[0].__name__
        for attr_name in dir(bases[0]):
            if not attr_name.startswith('_'):
                args_info = getfullargspec(getattr(bases[0], attr_name))
                task_name = '.'.join((base_name, attr_name))
                dct[attr_name] = CallerMetaBase._CalledTask(
                    task_name,
                    args_info
                )

        return ABCMeta.__new__(cls, name, bases, dct)
