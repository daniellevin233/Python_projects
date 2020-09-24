"""
Abstract class Command
"""

from abc import abstractmethod, ABC


class Command(ABC):
    """
    Type of command
    """
    @property
    @abstractmethod
    def type(self):
        return self.type

    """
    Responsible for translating the commands to binary
    """
    @abstractmethod
    def translate(self, symbol_table):
        pass
