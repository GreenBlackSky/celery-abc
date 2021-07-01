from abc import ABCMeta


class CallerMetaBase(ABCMeta):

    def _init_overriden(self, celery):
        self._celery = celery

    class _CalledTask:
        def __init__(self, name):
            self._name = name

        def __call__(self, kargs):
            # pass celery here
            # get args names
            print("Sending", self._name, kargs)

    def __new__(cls, name, bases, dct):
        dct['__init__'] = CallerMetaBase._init_overriden
        for attr_name in dir(bases[0]):
            if not attr_name.startswith('__'):
                dct[attr_name] = CallerMetaBase._CalledTask(attr_name)

        return ABCMeta.__new__(cls, name, bases, dct)
