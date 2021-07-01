from abc import ABC
from celery_abc import CallerMetaBase, RecieverMetaBase


class Interface(ABC):
    @abstractmethod
    def method_1(self, arg):
        pass

    @abstractmethod
    def method_2(self, arg):
        pass


class Caller(Interface, metaclass=CallerMetaBase):
    pass


class Reciever(Interface, metaclass=RecieverMetaBase):
    def method_1(self, arg):
        print("Recieve method_1", arg)
        self.method_2(arg)

    def method_2(self, arg):
        print("Recieve method_2", arg)


Caller("CELERY").method_1(1)
Reciever("CELERY").method_1(2)
