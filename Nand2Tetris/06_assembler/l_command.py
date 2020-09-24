"""
L-Command class
"""

import re


class LCommand():
    def __init__(self, command_str):
        self.__loop_name = ''
        self.parse(command_str)

    @property
    def type(self):
        return 'L'

    def parse(self, command_str):
        loop_name = re.search(r'^\(.+\)', command_str).group()
        self.__loop_name = loop_name[1:len(loop_name) - 1]

    def get_loop_name(self):
        return self.__loop_name
