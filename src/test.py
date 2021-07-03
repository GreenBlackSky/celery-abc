"""Test how does it work."""

from abc import ABC, abstractmethod
from unittest import TestCase

from celery_abc import CallerMetaBase, WorkerMetaBase


class Interface(ABC):
    @abstractmethod
    def method_1(self, arg):
        pass

    @abstractmethod
    def method_2(self, arg):
        pass

    @abstractmethod
    def method_3(self, arg):
        pass


class Caller(Interface, metaclass=CallerMetaBase):
    pass


class Reciever(Interface, metaclass=WorkerMetaBase):
    def method_1(self, arg):
        print("Recieve method_1", arg)
        self.method_2(arg)

    def method_2(self, arg):
        print("Recieve method_2", arg)
        self.method_3(arg)

    def method_3(self, arg):
        print("Recieve method_3", arg)


class celery_mock:
    def get(self):
        pass

    def task(self, *args, **kargs):
        return lambda x: x

    def send_task(self, name, kwargs):
        print("Calling task", name, kwargs)
        return self


class TestJoke(TestCase):

    def test_caller(self):
        Caller(celery_mock()).method_1(1)

    def test_worker(self):
        Reciever(celery_mock()).method_1(2)
