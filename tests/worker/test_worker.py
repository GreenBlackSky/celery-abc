"""Test how does it work."""

import os

from celery import Celery
from celery_abc import WorkerMetaBase

from shared.interface import Interface


class Worker(Interface, metaclass=WorkerMetaBase):
    """Worker class exmple."""

    def add(self, a, b):
        """Return sum of two values."""
        print("add <<< ", a, b)
        ret = a + b
        print("add >>>", ret)
        return ret

    def add_positional(self, a, b, c, d):
        """Sum up all given args."""
        print("add_positional <<<", a, b, c, d)
        ret = self.add(self.add(a, b), self.add(c, d))
        print("add_positional >>>", ret)
        return ret

    # def add_list(self, *args):
    #     """Sum up all given args."""
    #     print("add_list <<< *args", args)
    #     ret = sum(args)
    #     print("add_list >>>", ret)
    #     return ret

    # def add_dict(self, **kargs):
    #     """Sum up all given args."""
    #     print("add_dict <<<", kargs)
    #     ret = sum(kargs.values())
    #     print("add_dict >>>", ret)
    #     return ret

    # def add_positionald_and_list(self, a, b, *args):
    #     """Sum up all given args."""
    #     print("add_positionald_and_list <<<", a, b, args)
    #     ret = a + b + sum(args)
    #     print("add_positionald_and_list >>>", ret)
    #     return ret

    # def add_positional_and_dict(self, a, b, **kargs):
    #     """Sum up all given args."""
    #     print("add_positional_and_dict <<<", a, b, kargs)
    #     ret = a + b + sum(kargs.values())
    #     print("add_positional_and_dict >>>", ret)
    #     return ret

    # def add_list_and_dict(self, *args, **kargs):
    #     """Sum up all given args."""
    #     print("add_list_and_dict <<<", args, kargs)
    #     ret = sum(args) + sum(kargs.values())
    #     print("add_list_and_dict >>>", ret)
    #     return ret

    # def add_positional_list_and_dict(self, a, b, *args, **kargs):
    #     """Sum up all given args."""
    #     print("add_positional_list_and_dict <<<", a, b, args, kargs)
    #     ret = a + b + sum(args) + sum(kargs)
    #     print("add_positional_list_and_dict >>>", ret)
    #     return ret


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
