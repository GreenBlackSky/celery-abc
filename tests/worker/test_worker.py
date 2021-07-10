"""Test how does it work."""

import os

from celery import Celery
from celery_abc import WorkerMetaBase

from shared.interface import Interface


class Worker(Interface, metaclass=WorkerMetaBase):
    """Worker class exmple."""

    def add_three(self, a, b, c):
        """Implementaition of interface method."""
        print("add_three <<<", a, b, c)
        ret = self.add(a, self.add(b, c))
        print("add_three >>>", ret)
        return ret

    def add(self, a, b):
        """Implementaition of interface method."""
        print("add <<< ", a, b)
        ret = a + b
        print("add >>>", ret)
        return ret


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
