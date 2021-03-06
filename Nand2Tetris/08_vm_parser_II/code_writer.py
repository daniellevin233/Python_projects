"""
Writer Class for writing to asm file given processed commands of VM language
"""

import os
from vm_parser import VMParser


class CodeWriter:
    """
    Writer class for writing to asm file given processed commands of VM language
    """

    """ Mapping of constant memory segments from their names in vm language to their names in asm language"""
    MEMORY_SEGMENTS_MAP = {'constant': 'R0',
                           'local': 'LCL',
                           'argument': 'ARG',
                           'this': 'THIS',
                           'that': 'THAT',
                           'temp': 'R5'}

    return_index = 0
    cur_loop_index = 0

    #  asm commands implementation

    @staticmethod
    def INIT():
        return """// init
@256
D=A
@SP
M=D
@Sys.init
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5 // ARG = SP-5
D=A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Sys.init // goto function
0;JMP 
"""
    @staticmethod
    def C_PUSH():
        return """// push
@SP
A=M
M=D
@SP
M=M+1
"""

    @staticmethod
    def CONST_PUSH_PREFIX(arg1, arg2):
        return """//
@{1}
D=A
@{2}
A=A+D
D=A
""".format(arg1, arg2, CodeWriter.MEMORY_SEGMENTS_MAP[arg1])

    @staticmethod
    def TEMP_PUSH_PREFIX(arg1, arg2):
        return """//
@{1}
D=A
@{2}
A=A+D
D=M
""".format(arg1, arg2, CodeWriter.MEMORY_SEGMENTS_MAP[arg1])  # TODO why arg1?

    @staticmethod
    def REG_SEG_PUSH_PREFIX(arg1, arg2):
        return """// set current memory index for push
@{1} // calc address
D=A
@{2}
D=M+D
A=D
D=M
""".format(arg1, arg2, CodeWriter.MEMORY_SEGMENTS_MAP[arg1])

    @staticmethod
    def POINTER_PUSH_PREFIX(this_or_that):
        return """// access this or that content for push
@{0}
D=M
""".format(this_or_that)

    @staticmethod
    def STATIC_PUSH_PREFIX(vm_prefix, arg2):
        return """//
@{0}.{1}
D=M
""".format(vm_prefix, arg2)

    @staticmethod
    def TEMP_POP_PREFIX(arg1, arg2):
        return """//
@{1} // calc address
D=A
@{2}
A=A+D
D=A
@R13
M=D
""".format(arg1, arg2, CodeWriter.MEMORY_SEGMENTS_MAP[arg1])

    @staticmethod
    def STATIC_POP_PREFIX(vm_prefix, arg2):
        return """//
@{0}.{1}
D=A
@R13
M=D
""".format(vm_prefix, arg2)

    @staticmethod
    def REG_SEG_POP_PREFIX(arg1, arg2):
        return """// set current memory index for pop
@{1} // calc address
D=A
@{2}
A=M+D
D=A
@R13
M=D
""".format(arg1, arg2, CodeWriter.MEMORY_SEGMENTS_MAP[arg1])

    @staticmethod
    def POINTER_POP_PREFIX(this_or_that):
        return """// access this or that content for pop
@{0}
D=A
@R13
M=D
""".format(this_or_that)

    @staticmethod
    def C_POP():
        return """// pop {0} {1} 
@SP
M=M-1
A=M
D=M
@R13
A=M // goto MEMSEG i
M=D
"""

    #  binary commands

    @staticmethod
    def ADD_COMMAND():
        return """// add
@SP // pop first
M=M-1
A=M
D=M
@R15
M=D
@SP // pop second
M=M-1
A=M
D=M
@R15
MD=D+M
@SP // push result
A=M
M=D
@SP
M=M+1
"""

    @staticmethod
    def SUB_COMMAND():
        return """// sub
@SP // pop second
M=M-1
A=M
D=M
@R14
M=D
@SP // pop first
M=M-1
A=M
D=M
@R15
M=D
@R14
MD=D-M
@SP // push result
A=M
M=D
@SP
M=M+1
"""

    @staticmethod
    def AND_COMMAND():
        return '// and\n' + CodeWriter.ADD_COMMAND().replace('D+M', 'D&M')

    @staticmethod
    def OR_COMMAND():
        return '// or\n' + CodeWriter.ADD_COMMAND().replace('D+M', 'D|M')

    @staticmethod
    def OVERFLOW():
        return """// dealing with overflow
@SP // pop second
M=M-1
A=M
D=M
@R14
M=D
@SP // pop first
M=M-1
A=M
D=M
@R13
M=D
@GOOD_INPUT_{0}
D;JEQ
@R14
D=M
@GOOD_INPUT_{0}
D;JEQ
(BAD_INPUT_{0}) // check sign of first num
@R13
D=M
@NEG_{0}
D;JLT
@POS_{0}
0;JMP
(NEG_{0}) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_{0} // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_{0}
0;JMP
(POS_{0}) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_{0} // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_{0}
0;JMP
(MAKE_VALUE_ZERO_{0})
@R14 // Make second num zero
M=0""".format(CodeWriter.cur_loop_index)

    @staticmethod
    def GT_COMMAND():
        CodeWriter.cur_loop_index += 1
        return CodeWriter.OVERFLOW() + """
// gt
(GOOD_INPUT_{0})
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_{0}
D;JGT
(FALSE_{0})
@R15
M=0
(END_{0})
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
""".format(CodeWriter.cur_loop_index)

    @staticmethod
    def EQ_COMMAND():
        CodeWriter.cur_loop_index += 1
        return CodeWriter.OVERFLOW() + """
// eq
(GOOD_INPUT_{0})
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_{0}
D;JEQ
(FALSE_{0})
@R15
M=0
(END_{0})
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
""".format(CodeWriter.cur_loop_index)

    @staticmethod
    def LT_COMMAND():
        CodeWriter.cur_loop_index += 1
        return CodeWriter.OVERFLOW() + """
// lt
(GOOD_INPUT_{0})
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_{0}
D;JLT
(FALSE_{0})
@R15
M=0
(END_{0})
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
""".format(CodeWriter.cur_loop_index)

    #  unary commands

    @staticmethod
    def NEG_COMMAND():
        return """// neg
@SP // pop number
M=M-1
A=M
D=M
@R15
MD=-D
@SP // push result
A=M
M=D
@SP
M=M+1
"""

    @staticmethod
    def NOT_COMMAND():
        return '// not\n' + CodeWriter.NEG_COMMAND().replace('-D', '!D')

    @staticmethod
    def LABEL_COMMAND(arg1, function_name):
        return "({1}${0})".format(arg1, function_name)

    @staticmethod
    def GOTO_COMMAND(arg1, function_name):
        return """// goto {0}
@{0}${1}
0;JMP        
""".format(function_name, arg1)

    @staticmethod
    def IF_GOTO_COMMAND(arg1, function_name):
        return """// if-goto {0} 
@SP // pop the topmost value from the stack
M=M-1
A=M
D=M
@{0}${1} // jump if value is -1
D;JNE
""".format(function_name, arg1)

    @staticmethod
    def CALL_COMMAND(arg1, arg2, function_name, index):
        return """// call {0} {1} 
@{2}$ret.{3} // push return address
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5 // ARG = SP-5-nArgs
D=A
@{1}
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@{0} // goto function
0;JMP 
({2}$ret.{3})
""".format(arg1, arg2, function_name, index)

    @staticmethod
    def FUNCTION_COMMAND(arg1, arg2):
        return """// function {0} {1} 
({0})
@{1}
D=A
({0}$PUSH_LOOP) // SimpleFunction.test
@{0}$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@{0}$PUSH_LOOP
0;JMP
({0}$END)
""".format(arg1, arg2)

    @staticmethod
    def RETURN_COMMAND(function_name):
        return """// return 
@LCL
D=M
@{0}$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@{0}$ret_address // return-address temporary variable
M=D
@SP  // *ARG = pop()
M=M-1
A=M
D=M
@ARG
A=M // arg[0]
M=D
D=A
@SP // restore SP for caller
M=D+1
@{0}$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@{0}$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@{0}$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@{0}$frame
A=M-D
D=M
@LCL
M=D
@{0}$ret_address // goto the return-address
A=M
0;JMP
""".format(function_name)

    def __init__(self, asm_file_path):
        """
        Constructor of the code writer
        :param asm_file_path: Asm file path to be translated to
        """

        """ Asm file path to be translated to """
        self.__asm_file_path = asm_file_path

        """ The asm file itself """
        self.__asm_file = open(asm_file_path, 'w')

        """ VM file being processed currently"""
        self.__current_vm_file = ''

        """ Index representing counter of static variables for certain VM file """
        self.__current_static_index = 0

        self.__cur_function_name = ''

    def set_file_name(self, file_name):
        """
        Sets name of currently processed vm file
        :param file_name: new file name to be set
        """
        self.__current_static_index = 0
        self.__current_vm_file = file_name

    def get_command(self, command_type, arg1, arg2):
        """
        Determines the command being currently parsed by parameters parsed from line of vm file
        :param command_type: Type of the command parsed from the vm file
        :param arg1: First argument parsed from the vm file
        :param arg2: Second argument parsed from the vm file
        :return: Command implementation in asm language
        """
        if command_type == VMParser.CommandTypes.ARITHMETIC:
            return CodeWriter.ARITHM_COMMANDS_DICT[arg1]()

        elif command_type == VMParser.CommandTypes.LABEL:
            return CodeWriter.LABEL_COMMAND(arg1, self.__cur_function_name)

        elif command_type == VMParser.CommandTypes.GOTO:
            return CodeWriter.GOTO_COMMAND(arg1, self.__cur_function_name)

        elif command_type == VMParser.CommandTypes.IF_GOTO:
            return CodeWriter.IF_GOTO_COMMAND(arg1, self.__cur_function_name)

        elif command_type == VMParser.CommandTypes.CALL:
            command = CodeWriter.CALL_COMMAND(arg1, arg2, self.__cur_function_name, CodeWriter.return_index)
            CodeWriter.return_index += 1
            return command

        elif command_type == VMParser.CommandTypes.FUNCTION:
            self.__cur_function_name = arg1
            CodeWriter.return_index = 0
            return CodeWriter.FUNCTION_COMMAND(arg1, arg2)

        elif command_type == VMParser.CommandTypes.RETURN:
            return CodeWriter.RETURN_COMMAND(self.__cur_function_name)

        push_pop_command = ''
        if command_type == VMParser.CommandTypes.PUSH:
            if arg1 == 'constant':
                push_pop_command = CodeWriter.CONST_PUSH_PREFIX(arg1, arg2)
            elif arg1 == 'pointer':
                if arg2 == '0':
                    push_pop_command = CodeWriter.POINTER_PUSH_PREFIX('THIS')
                else:
                    push_pop_command = CodeWriter.POINTER_PUSH_PREFIX('THAT')
            elif arg1 == 'temp':
                push_pop_command = CodeWriter.TEMP_PUSH_PREFIX(arg1, arg2)
            elif arg1 == 'static':
                push_pop_command = CodeWriter.STATIC_PUSH_PREFIX(os.path.splitext(self.__current_vm_file)[0], arg2)
            else:
                push_pop_command = CodeWriter.REG_SEG_PUSH_PREFIX(arg1, arg2)

            push_pop_command += CodeWriter.C_PUSH()
        elif command_type == VMParser.CommandTypes.POP:
            if arg1 == 'pointer':
                if arg2 == '0':
                    push_pop_command = CodeWriter.POINTER_POP_PREFIX('THIS')
                else:
                    push_pop_command = CodeWriter.POINTER_POP_PREFIX('THAT')
            elif arg1 == 'temp':
                push_pop_command = CodeWriter.TEMP_POP_PREFIX(arg1, arg2)
            elif arg1 == 'static':
                push_pop_command = CodeWriter.STATIC_POP_PREFIX(os.path.splitext(self.__current_vm_file)[0], arg2)
            else:
                push_pop_command = CodeWriter.REG_SEG_POP_PREFIX(arg1, arg2)

            push_pop_command += CodeWriter.C_POP()

        return push_pop_command

    def write_init(self):
        self.__asm_file.write(CodeWriter.INIT())

    def write(self, command_type, arg1, arg2):
        """
        Writes asm command matching parameters given form vm file
        """
        command = self.get_command(command_type, arg1, arg2)
        for line in command.splitlines():
            self.__asm_file.write(line + '\n')

    def close(self):
        """
        Closes filled asm file
        """
        self.__asm_file.close()


CodeWriter.ARITHM_COMMANDS_DICT = {
    'add': CodeWriter.ADD_COMMAND,
    'sub': CodeWriter.SUB_COMMAND,
    'neg': CodeWriter.NEG_COMMAND,
    'eq': CodeWriter.EQ_COMMAND,
    'gt': CodeWriter.GT_COMMAND,
    'lt': CodeWriter.LT_COMMAND,
    'and': CodeWriter.AND_COMMAND,
    'or': CodeWriter.OR_COMMAND,
    'not': CodeWriter.NOT_COMMAND
}
