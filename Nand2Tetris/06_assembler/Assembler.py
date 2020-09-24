"""
Main flow of program.
Usage notes: Assembler <asm_file_path>
"""

import sys
from asm_parser import Parser
from symbol_table import SymbolTable
import os


def main(argv):
    if not check_args(argv):
        return

    #  extracting asm file to be processed
    asm_file_path = argv[1]

    #  creating a .hack file to contain asm file translation to hack machine language
    pre, post = os.path.splitext(asm_file_path)
    hack_file_path = pre + '.hack'

    with open(hack_file_path, 'w') as hack_file, open(asm_file_path) as asm_file:
        symbol_table = SymbolTable()
        first_pass(asm_file, symbol_table)
        second_pass(asm_file, hack_file, symbol_table)


def check_args(arg_list):
    return len(arg_list) == 2


#  first pass through the file - filling the table of symbols
def first_pass(asm_file, symbol_table):
    asm_parser = Parser(asm_file)
    while asm_parser.has_more_commands():
        command = asm_parser.advance()

        if command.type == 'L':
            symbol_table.add_entry(command.get_loop_name(), asm_parser.get_line_num())
    asm_file.seek(0)


#  second pass through the file - translating commands
def second_pass(asm_file, hack_file, symbol_table):
    asm_parser = Parser(asm_file)
    while asm_parser.has_more_commands():
        command = asm_parser.advance()

        #  dealing with commands of type A which may contain new variables declaration
        if command.type == 'A':
            if command.symbolic and not symbol_table.contains(command.get_symbol()):
                symbol_table.add_variable(command.get_symbol())
        if command.type == 'A' or command.type == 'C':
            binary_command = command.translate(symbol_table)
            hack_file.write(binary_command + '\n')


if __name__ == '__main__':
    main(sys.argv)
