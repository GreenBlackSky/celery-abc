"""Test how does it work."""

import os

from celery import Celery
from celery_abc import WorkerMetaBase

from shared.interface import Interface


class Worker(Interface, metaclass=WorkerMetaBase):
    """Worker class exmple."""

    def add(self, a, b):
        print("add <<< ", a, b)
        ret = a + b
        print("add >>>", ret)
        return ret

    def add_positional(self, a, b, c, d):
        print("add_positional <<<", a, b, c, d)
        ret = self.add(self.add(a, b), self.add(c, d))
        print("add_positional >>>", ret)
        return ret

    # def add_default(self, a=1, b=2, c=3, d=4):
    #     print("add_default <<<", a, b, c, d)
    #     ret = sum((a, b, c, d))
    #     print("add_default >>>", ret)

    # def add_default_2(self, a=1, b=2, c=3, d=4, e=5, f=6):
    #     print("add_default_2 <<<", a, b, c, d, e, f)
    #     ret = sum((a, b, c, d, e, f))
    #     print("add_default_2 >>>", ret)

    # def add_default_3(self, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8):
    #     print("add_default_3 <<<", a, b, c, d, e, f, g, h)
    #     ret = sum((a, b, c, d, e, f, g, h))
    #     print("add_default_3 >>>", ret)

    # def add_list(self, *args):
    #     print("add_list <<< *args", args)
    #     ret = sum(args)
    #     print("add_list >>>", ret)
    #     return ret

    # def add_dict(self, **kargs):
    #     print("add_dict <<<", kargs)
    #     ret = sum(kargs.values())
    #     print("add_dict >>>", ret)
    #     return ret

    # def add_positionald_and_default(self, a, b, c=3, d=4):
    #     pass

    # def add_positionald_and_list(self, a, b, *args):
    #     print("add_positionald_and_list <<<", a, b, args)
    #     ret = a + b + sum(args)
    #     print("add_positionald_and_list >>>", ret)
    #     return ret

    # def add_positional_and_dict(self, a, b, **kargs):
    #     print("add_positional_and_dict <<<", a, b, kargs)
    #     ret = a + b + sum(kargs.values())
    #     print("add_positional_and_dict >>>", ret)
    #     return ret

    # def add_default_and_list(self, a=1, b=2, *args):
    #     pass

    # def add_default_and_dict(self, a=1, b=2, **kargs):
    #     pass

    # def add_list_and_dict(self, *args, **kargs):
    #     print("add_list_and_dict <<<", args, kargs)
    #     ret = sum(args) + sum(kargs.values())
    #     print("add_list_and_dict >>>", ret)
    #     return ret

    # def add_positional_default_and_list(self, a, b=2, *args):
    #     pass

    # def add_positional_default_and_dict(self, a, b=2, **kargs):
    #     pass

    # def add_positional_list_and_dict(self, a, b, *args, **kargs):
    #     print("add_positional_list_and_dict <<<", a, b, args, kargs)
    #     ret = a + b + sum(args) + sum(kargs)
    #     print("add_positional_list_and_dict >>>", ret)
    #     return ret

    # def add_default_list_and_dict(self, a=1, b=2, *args, **kargs):
    #     pass

    # def add_positional_default_list_and_dict(self, a, b=2, *args, **kargs):
    #     pass


celery = Celery(
    broker='amqp://{}:{}@{}:{}//'.format(
        os.environ['RABBITMQ_DEFAULT_USER'],
        os.environ['RABBITMQ_DEFAULT_PASS'],
        os.environ['RABBITMQ_HOST'],
        os.environ['RABBITMQ_PORT']
    ),
    backend='rpc://'
)
worker = Worker(celery)
