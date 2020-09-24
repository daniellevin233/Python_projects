"""
Parser Class for reading from vm file and parsing its commands
"""

from enum import Enum


class VMParser:
    """
    Parser Class dealing with parsing of VM files
    """
    COMMENT_STRING = '//'

    class CommandTypes(Enum):
        """
        Class enumerating all possible commands types
        """
        ARITHMETIC = "C_ARITHMETIC"
        PUSH = "C_PUSH"
        POP = "C_POP"
        LABEL = "C_LABEL"
        GOTO = "C_GOTO"
        IF = "C_IF"
        FUNCTION = "C_FUNCTION"
        RETURN = "C_RETURN"
        CALL = "C_CALL"

    def __init__(self, vm_file_path):
        self.__vm_file = open(vm_file_path)
        self.__command_type = VMParser.CommandTypes
        self.__current_command = ''

    def has_more_commands(self):
        """
        :return: True iff processed vm file has more commands to be translated
        """
        while True:
            line = self.__vm_file.readline()

            # If line is EOF no more commands are left
            if line == '':
                self.__vm_file.close()
                return False

            cleaned_line = self.clean_line(line)
            split_line = cleaned_line.split()
            if self.is_command(split_line):
                self.advance(split_line)
                return True

    @staticmethod
    def clean_line(line):
        """
        Cleans line from comments and whitespaces (both trimming and internal whitespaces omitting)
        :param line: line to be cleaned
        :return: cleaned version of line
        """
        # Check if handles multiple spaces in line
        no_comment_line = line.split(VMParser.COMMENT_STRING)[0]
        stripped_line = no_comment_line.strip()
        return stripped_line

    def is_command(self, line_arr):
        """
        Method initializes the command_type field with relevant command in case valid line was inserted
        :param line_arr: array containing split elements of line
        :return: True iff given elements may represent one among existing commands
        """
        if len(line_arr) == 0:
            return False

        is_command = False
        if self.is_arithmetic_command(line_arr):
            self.__command_type = VMParser.CommandTypes.ARITHMETIC
            is_command = True
        elif self.is_push_command(line_arr):
            self.__command_type = VMParser.CommandTypes.PUSH
            is_command = True
        elif self.is_pop_command(line_arr):
            self.__command_type = VMParser.CommandTypes.POP
            is_command = True

        return is_command

    @staticmethod
    def is_arithmetic_command(line_arr):
        """
        :return: True iff given array represents one of arithmetic commands
        """
        return line_arr[0] in ("add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not")

    @staticmethod
    def is_push_command(line_arr):
        """
        :return: True iff given array represents push command
        """
        return line_arr[0] == "push"

    @staticmethod
    def is_pop_command(line_arr):
        """
        :return: True iff given array represents pop command
        """
        return line_arr[0] == "pop"

    def advance(self, line_arr):
        """
        Advances current command to be the next line in the vm file
        """
        self.__current_command = line_arr

    def command_type(self):
        """
        Getter for command type of the command being currently parsed
        """
        return self.__command_type

    def arg1(self):
        """
        Getter for first argument of the command being currently parsed
        """
        if self.__command_type == VMParser.CommandTypes.ARITHMETIC:
            return self.__current_command[0]
        else:
            return self.__current_command[1]

    def arg2(self):
        """
        Getter for second argument of the command being currently parsed
        """
        return self.__current_command[2]
