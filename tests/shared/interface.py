"""This is an example of interface module."""

from abc import ABC, abstractmethod


class Interface(ABC):
    """Interface example."""

    @abstractmethod
    def add_three(self, a, b, c):
        """Add three values."""
        pass

    @abstractmethod
    def add(self, a, b):
        """Add two values."""
        pass
