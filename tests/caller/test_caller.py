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


if __name__ == '__main__':
    while True:
        a, b, c = 1, 2, 3
        print("add_three <<<", a, b, c)
        result = caller.add_three(a, b, c)
        print("add_three >>>", result)
        sleep(5)
