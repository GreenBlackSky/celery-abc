"""This is an example of interface module."""

from abc import ABC, abstractmethod


class Interface(ABC):
    """Interface example."""

    @abstractmethod
    def add(self, a, b):
        """Add two values."""
        pass

    @abstractmethod
    def add_positional(self, a, b, c, d):
        """Add four values."""
        pass

    # @abstractmethod
    # def add_list(self, *args):
    #     """Check stuff."""
    #     pass

    # @abstractmethod
    # def add_dict(self, **kargs):
    #     """Check stuff."""
    #     pass

    # @abstractmethod
    # def add_positionald_and_list(self, a, b, *args):
    #     """Check stuff."""
    #     pass

    # @abstractmethod
    # def add_positional_and_dict(self, a, b, **kargs):
    #     """Check stuff."""
    #     pass

    # @abstractmethod
    # def add_list_and_dict(self, *args, **kargs):
    #     """Check stuff."""
    #     pass

    # @abstractmethod
    # def add_positional_list_and_dict(self, a, b, *args, **kargs):
    #     """Check stuff."""
    #     pass
