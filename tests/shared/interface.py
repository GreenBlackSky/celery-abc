"""This is an example of interface module."""

from abc import ABC, abstractmethod


class Interface(ABC):
    """Interface example."""

    @abstractmethod
    def do_some_stuff(self, arg):
        """Example method that doesn't actually do stuff."""
        pass

    @abstractmethod
    def do_more_stuff(self, arg):
        """Example method, that doesn't actually do anything."""
        pass
