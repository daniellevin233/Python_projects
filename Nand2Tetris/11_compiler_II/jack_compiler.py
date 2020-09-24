"""
Main flow of program.
Usage notes: JackCompiler <jack_file_path> or JackCompiler <jack_file_dir>
"""

import sys
from vm_writer import VMWriter
from compilation_engine import CompilationEngine
import os


def main(argv):
    """
    Main flow of program dealing with extracting files for reading and initializing files to translate into
    """
    if not check_args(argv):
        return

    #  extracting jack file to be processed
    jack_files_path = argv[1]

    #  creating a .vm file to contain jack files translation to vm language
    if os.path.isdir(jack_files_path):
        for file in os.listdir(jack_files_path):
            if file.endswith(".jack"):
                vm_file_name = "{0}/{1}.vm".format(jack_files_path, os.path.splitext(os.path.basename(file))[0])
                vm_writer = VMWriter(vm_file_name)
                CompilationEngine('{0}/{1}'.format(jack_files_path, file), vm_writer)
    else:
        vm_file_name = "{0}.vm".format(os.path.splitext(jack_files_path)[0])
        vm_writer = VMWriter(vm_file_name)
        CompilationEngine(jack_files_path, vm_writer)


def check_args(arg_list):
    return len(arg_list) == 2


if __name__ == '__main__':
    main(sys.argv)