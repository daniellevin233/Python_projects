"""
C-command class
"""

from command import Command


class CCommand(Command):

    C_COMMAND_COMP_MAPPING = {
        '0': '1110101010',  # a=0
        '1': '1110111111',
        '-1': '1110111010',
        'D': '1110001100',
        'A': '1110110000',
        '!D': '1110001101',
        '!A': '1110110011',
        '-D': '1110001111',
        '-A': '1110110011',
        'D+1': '1110011111',
        'A+1': '1110110111',
        'D-1': '1110001110',
        'A-1': '1110110010',
        'D+A': '1110000010',
        'D-A': '1110010011',
        'A-D': '1110000111',
        'D&A': '1110000000',
        'D|A': '1111010101',
        'M': '1111110000',  # a=1
        '!M': '1111110001',
        '-M': '1111110011',
        'M+1': '1111110111',
        'M-1': '1111110010',
        'D+M': '1111000010',
        'D-M': '1111010011',
        'M-D': '1111000111',
        'D&M': '1111000000',
        'D|M': '1111010101',
        'D<<': '1010110000',  # additional requirements
        'D>>': '1010010000',
        'A<<': '1010100000',
        'A>>': '1010000000',
        'M<<': '1011100000',
        'M>>': '1011000000',
    }

    C_COMMAND_DEST_MAPPING = {
        '': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }

    C_COMMAND_JUMP_MAPPING = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }

    def __init__(self, command_str):
        self.__jump = ''
        self.__dest = ''
        self.__comp = ''
        self.parse(command_str)

    def parse(self, command_str):
        remaining_str = command_str
        if ';' in remaining_str:
            divided_by_semicolon = remaining_str.split(';')
            self.__jump = divided_by_semicolon[1]
            remaining_str = divided_by_semicolon[0]

        if '=' in remaining_str:
            divided_by_equal = remaining_str.split('=')
            self.__dest = divided_by_equal[0]
            remaining_str = divided_by_equal[1]

        self.__comp = remaining_str

    @property
    def type(self):
        return 'C'

    def translate(self, symbol_table):
        return CCommand.C_COMMAND_COMP_MAPPING.get(self.__comp) + \
               CCommand.C_COMMAND_DEST_MAPPING.get(self.__dest) + \
               CCommand.C_COMMAND_JUMP_MAPPING.get(self.__jump)
