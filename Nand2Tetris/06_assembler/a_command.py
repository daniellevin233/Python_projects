"""
A-Command class
"""

from command import Command
import re
from numpy import binary_repr


class ACommand(Command):

    def __init__(self, command_str):
        self.__symbol = re.search(r'.+', command_str[1:]).group()

    @property
    def type(self):
        return 'A'

    @property
    def symbolic(self):
        return not self.__symbol.isdigit()

    def get_symbol(self):
        return self.__symbol

    def translate(self, symbol_table):
        if symbol_table.contains(self.__symbol):
            self.__symbol = symbol_table.get_address(self.__symbol)
        return '0' + binary_repr(int(self.__symbol), width=15)
