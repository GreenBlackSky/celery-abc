"""Register methods of implementation class as celery tasks."""


from abc import ABCMeta
from functools import partial, update_wrapper


class WorkerMetaBase(ABCMeta):
    """
    Use as metaclass when impementing the Interface.

    It registers all public methods as celery tasks
    with name like `Classname.methodname`.
    And it replaces first `self` argument of given methods with
    the `HUB` object. HUB object is static object, that has all the
    public methods of child class but cannot access any variables.
    It is a tool for creating stateless services.

    Alos, replaces constructor `__init__` of base method with the
    constructor of it's own. It takes one argument that is a celery app.
    """

    def _init_overriden(self, celery):
        self._celery = celery
        for method_name in dir(self):
            if not method_name.startswith('_'):
                task_name = '.'.join((self._base_name, method_name))
                method = getattr(self, method_name)
                self._celery.task(name=task_name)(method)

    def __new__(cls, name, bases, dct):
        """
        Register methods of implementation as celery tasks.

        Also, replace self in given methods with HUB object.
        Hub is global, it has all public methods of the imlementation.
        But it is incapable of keeping any instance variables.
        Remember - this class is a tool for creating stateless services.
        """
        hub = type('HUB', (), {})
        dct['__init__'] = WorkerMetaBase._init_overriden
        dct['_base_name'] = name
        for attr_name, method in dct.items():
            if not attr_name.startswith('_'):
                partial_method = partial(method, hub)
                update_wrapper(partial_method, method)
                setattr(hub, attr_name, partial_method)
                dct[attr_name] = partial_method
        return ABCMeta.__new__(cls, name, bases, dct)
