"""Test how does it work."""

import os

from celery import Celery
from celery_abc import WorkerMetaBase

from shared.interface import Interface


class Worker(Interface, metaclass=WorkerMetaBase):
    """Worker class exmple."""

    def do_some_stuff(self, arg):
        """Implementaition of interface method."""
        print("Recieve method_1", arg)
        self.do_more_stuff(arg)

    def do_more_stuff(self, arg):
        """Implementaition of interface method."""
        print("Recieve method_2", arg)
        self.method_3(arg)


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
