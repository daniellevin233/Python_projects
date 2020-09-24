"""
Main flow of program.
Usage notes: VMtranslator <vm_file_path> or VMtranslator <vm_file_dir>
"""

import sys
from vm_parser import VMParser
from code_writer import CodeWriter
import os


def main(argv):
    """
    Main flow of program dealing with extracting files for reading and initializing files to translate into
    """
    if not check_args(argv):
        return

    #  extracting asm file to be processed
    vm_files_path = argv[1]

    #  creating a .asm file to contain vm files translation to hack machine language
    if os.path.isdir(vm_files_path):
        dir_name = os.path.basename(vm_files_path)
        asm_file_name = "{0}/{1}.asm".format(vm_files_path, dir_name)
        code_writer = CodeWriter(asm_file_name)
        code_writer.write_init()
        for file in os.listdir(vm_files_path):
            if file.endswith(".vm"):
                code_writer.set_file_name(file)
                vm_parser = VMParser('{0}/{1}'.format(vm_files_path, file))
                translate_vm_file(code_writer, vm_parser)
    else:
        asm_file_name = "{0}.asm".format(os.path.splitext(vm_files_path)[0])
        code_writer = CodeWriter(asm_file_name)
        code_writer.write_init()
        code_writer.set_file_name(vm_files_path)
        vm_parser = VMParser(vm_files_path)
        translate_vm_file(code_writer, vm_parser)


def check_args(arg_list):
    return len(arg_list) == 2


def translate_vm_file(code_writer, vm_parser):
    """
    Main flow of translation process
    :param code_writer: object writing to the asm file
    :param vm_parser: object parsing vm file
    """
    while vm_parser.has_more_commands():
        arg2 = None
        if vm_parser.command_type() in (vm_parser.CommandTypes.PUSH, vm_parser.CommandTypes.POP,
                                        vm_parser.CommandTypes.CALL, vm_parser.CommandTypes.FUNCTION):
            arg2 = vm_parser.arg2()

        code_writer.write(vm_parser.command_type(), vm_parser.arg1(), arg2)


if __name__ == '__main__':
    main(sys.argv)
