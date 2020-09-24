
from command_factory import *


class Parser:
    """
    This class is responsible for the parsing of the ASM file
    """
    COMMENT_STRING = '//'

    ADDRESS_SYMBOL = '@'
    """ Symbol denoting beginning of A-command in asm files """

    def __init__(self, asm_file):
        """
        Constructor of parser
        :param asm_file: asm file to be parsed
        """

        self.__asm_file = asm_file
        """ Asm file to be parsed """

        self.__curr_line = ''
        """ Current chosen line in given asm file """

        self.__line_num = 0
        """ Current line number in output file """

    def get_line_num(self):
        return self.__line_num

    def has_more_commands(self):
        """
        Method aimed at checking whether the asm file associated with this instance has more
        commands to be translated, i.e. A or C commands
        :return: boolean: true iff asm file still has any commands to be translated
        """
        while True:
            self.__curr_line = self.__asm_file.readline()
            # If line is EOF no more commands are left
            if self.__curr_line == '':
                return False

            self.clean_line()
            if Parser.is_command(self.__curr_line):
                return True

    def clean_line(self):
        """
        Cleans line from comments and whitespaces (both trimming and internal whitespaces omitting)
        :param line:
        :return:
        """
        line = self.__curr_line.split(Parser.COMMENT_STRING)[0]
        self.__curr_line = line.replace(' ', '').strip()

    def advance(self):
        """
        Advance to the next command in asm file, and process this command by creating relevant command object
        :return: Command object
        """
        command = CommandFactory.create(self.__curr_line)
        if command.type != 'L':
            self.__line_num += 1
        return command

    @staticmethod
    def is_command(line_str):
        """
        Check whether given line is either A-command or C-command specification
        :param line_str: line from asm file
        :return: boolean
        """
        return len(line_str) != 0 and (Parser.is_a_command(line_str) or Parser.is_c_command(line_str) or
                                       Parser.is_l_command(line_str))

    @staticmethod
    def is_a_command(command_str):
        """
            Check whether given line is A-command specification
            :param command_str: line from asm file
            :return: boolean
        """
        return command_str[0] == Parser.ADDRESS_SYMBOL

    @staticmethod
    def is_c_command(command_str):
        """
            Check whether given line is C-command specification
            :param command_str: line from asm file
            :return: boolean
        """
        c_command_starters = tuple(CCommand.C_COMMAND_COMP_MAPPING.keys())
        return command_str.startswith(c_command_starters)

    @staticmethod
    def is_l_command(command_str):
        """
            Check whether given line is a L-command specification
            :param command_str: line from asm file
            :return: boolean
        """
        return command_str.startswith('(')
