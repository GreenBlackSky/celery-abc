"""This is an example of interface module."""

from abc import ABC, abstractmethod


class Interface(ABC):
    """Interface example."""

    @abstractmethod
    def add_three(self, a, b, c):
        """Example method that doesn't actually do stuff."""
        pass

    @abstractmethod
    def add(self, a, b):
        """Example method, that doesn't actually do anything."""
        pass
