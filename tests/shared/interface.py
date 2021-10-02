"""This is an example of interface module."""

from abc import ABC, abstractmethod


class Interface(ABC):
    """Interface example."""

    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def add_positional(self, a, b, c, d):
        pass

    # @abstractmethod
    # def add_default(self, a=1, b=2, c=3):
    #     pass

    # @abstractmethod
    # def add_default_2(self, a=1, b=2, c=3, d=4, e=5, f=6):
    #     pass

    # @abstractmethod
    # def add_default_3(self, a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8):
    #     pass

    # @abstractmethod
    # def add_list(self, *args):
    #     pass

    # @abstractmethod
    # def add_dict(self, **kargs):
    #     pass

    # @abstractmethod
    # def add_positionald_and_default(self, a, b, c=3, d=4):
    #     pass

    # @abstractmethod
    # def add_positionald_and_list(self, a, b, *args):
    #     pass

    # @abstractmethod
    # def add_positional_and_dict(self, a, b, **kargs):
    #     pass

    # @abstractmethod
    # def add_default_and_list(self, a=1, b=2, *args):
    #     pass

    # @abstractmethod
    # def add_default_and_dict(self, a=1, b=2, **kargs):
    #     pass

    # @abstractmethod
    # def add_list_and_dict(self, *args, **kargs):
    #     pass

    # @abstractmethod
    # def add_positional_default_and_list(self, a, b=2, *args):
    #     pass

    # @abstractmethod
    # def add_positional_default_and_dict(self, a, b=2, **kargs):
    #     pass

    # @abstractmethod
    # def add_positional_list_and_dict(self, a, b, *args, **kargs):
    #     pass

    # @abstractmethod
    # def add_default_list_and_dict(self, a=1, b=2, *args, **kargs):
    #     pass

    # @abstractmethod
    # def add_positional_default_list_and_dict(self, a, b=2, *args, **kargs):
    #     pass
