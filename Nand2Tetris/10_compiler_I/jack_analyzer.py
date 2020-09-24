"""
Main flow of program.
Usage notes: JackAnalyzer <jack_file_path> or JackAnalyzer <jack_file_dir>
"""

import sys
from jack_tokenizer import JackTokenizer
from compilation_engine import CompilationEngine
import os


def main(argv):
    """
    Main flow of program dealing with extracting files for reading and initializing files to translate into
    """
    if not check_args(argv):
        return

    #  extracting asm file to be processed
    jack_files_path = argv[1]

    #  creating a .asm file to contain vm files translation to hack machine language
    if os.path.isdir(jack_files_path):
        for file in os.listdir(jack_files_path):
            if file.endswith(".jack"):
                xml_file_name = "{0}/{1}.xml".format(jack_files_path, os.path.splitext(os.path.basename(file))[0])
                CompilationEngine('{0}/{1}'.format(jack_files_path, file), xml_file_name)
    else:
        xml_file_name = "{0}.xml".format(os.path.splitext(jack_files_path)[0])
        CompilationEngine(jack_files_path, xml_file_name)


def check_args(arg_list):
    return len(arg_list) == 2


if __name__ == '__main__':
    main(sys.argv)