"""Test how does caller work."""

import os
from time import sleep

from celery import Celery
from celery_abc import CallerMetaBase

from shared.interface import Interface


class Caller(Interface, metaclass=CallerMetaBase):
    """Caller class example."""

    pass


celery = Celery(
    broker='amqp://{}:{}@{}:{}//'.format(
        os.environ['RABBITMQ_DEFAULT_USER'],
        os.environ['RABBITMQ_DEFAULT_PASS'],
        os.environ['RABBITMQ_HOST'],
        os.environ['RABBITMQ_PORT']
    ),
    backend='rpc://'
)
caller = Caller(celery)
while True:
    print("!!! Requesting task with arg 1")
    result = caller.add_three(1, 2, 3)
    print("!!! Got result:", result)
    sleep(5)
