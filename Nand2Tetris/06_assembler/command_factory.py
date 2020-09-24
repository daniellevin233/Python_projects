"""
Command Factory
"""

from c_command import CCommand
from a_command import ACommand
from l_command import LCommand
import asm_parser


class CommandFactory:

    @staticmethod
    def create(command_str):
        if asm_parser.Parser.is_a_command(command_str):
            return ACommand(command_str)
        elif asm_parser.Parser.is_c_command(command_str):
            return CCommand(command_str)
        elif asm_parser.Parser.is_l_command(command_str):
            return LCommand(command_str)
