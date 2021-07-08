"""Test how does it work."""

import os

from celery import Celery
from celery_abc import WorkerMetaBase

from shared.interface import Interface


class Worker(Interface, metaclass=WorkerMetaBase):
    """Worker class exmple."""

    def add_three(self, a, b, c):
        """Implementaition of interface method."""
        print("!!! Recieve call for 'do_some_stuff' with", a, b, c)
        return self.add(a, self.add(b, c))

    def add(self, a, b):
        """Implementaition of interface method."""
        print("!!! Recieve call for do_more_stuff 'with' ", a, b)
        return a + b


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
