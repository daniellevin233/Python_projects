// init
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
// function Main.fibonacci 0 
(Main.fibonacci)
@0
D=A
(Main.fibonacci$PUSH_LOOP) // SimpleFunction.test
@Main.fibonacci$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Main.fibonacci$PUSH_LOOP
0;JMP
(Main.fibonacci$END)
// set current memory index for push
@0 // calc address
D=A
@ARG
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@2
D=A
@R0
A=A+D
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// dealing with overflow
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
@GOOD_INPUT_1
D;JEQ
@R14
D=M
@GOOD_INPUT_1
D;JEQ
(BAD_INPUT_1) // check sign of first num
@R13
D=M
@NEG_1
D;JLT
@POS_1
0;JMP
(NEG_1) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_1 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_1
0;JMP
(POS_1) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_1 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_1
0;JMP
(MAKE_VALUE_ZERO_1)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_1)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_1
D;JLT
(FALSE_1)
@R15
M=0
(END_1)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// if-goto Main.fibonacci 
@SP // pop the topmost value from the stack
M=M-1
A=M
D=M
@Main.fibonacci$IF_TRUE // jump if value is -1
D;JNE
// goto Main.fibonacci
@Main.fibonacci$IF_FALSE
0;JMP        
(Main.fibonacci$IF_TRUE)
// set current memory index for push
@0 // calc address
D=A
@ARG
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
// return 
@LCL
D=M
@Main.fibonacci$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Main.fibonacci$ret_address // return-address temporary variable
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
@Main.fibonacci$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Main.fibonacci$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Main.fibonacci$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Main.fibonacci$frame
A=M-D
D=M
@LCL
M=D
@Main.fibonacci$ret_address // goto the return-address
A=M
0;JMP
(Main.fibonacci$IF_FALSE)
// set current memory index for push
@0 // calc address
D=A
@ARG
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@2
D=A
@R0
A=A+D
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// sub
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
// call Main.fibonacci 1 
@Main.fibonacci$ret.0 // push return address
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
@1
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci // goto function
0;JMP 
(Main.fibonacci$ret.0)
// set current memory index for push
@0 // calc address
D=A
@ARG
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@1
D=A
@R0
A=A+D
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// sub
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
// call Main.fibonacci 1 
@Main.fibonacci$ret.1 // push return address
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
@1
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci // goto function
0;JMP 
(Main.fibonacci$ret.1)
// add
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
// return 
@LCL
D=M
@Main.fibonacci$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Main.fibonacci$ret_address // return-address temporary variable
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
@Main.fibonacci$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Main.fibonacci$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Main.fibonacci$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Main.fibonacci$frame
A=M-D
D=M
@LCL
M=D
@Main.fibonacci$ret_address // goto the return-address
A=M
0;JMP
// function Sys.init 0 
(Sys.init)
@0
D=A
(Sys.init$PUSH_LOOP) // SimpleFunction.test
@Sys.init$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Sys.init$PUSH_LOOP
0;JMP
(Sys.init$END)
//
@4
D=A
@R0
A=A+D
D=A
// push
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1 
@Sys.init$ret.0 // push return address
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
@1
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Main.fibonacci // goto function
0;JMP 
(Sys.init$ret.0)
(Sys.init$WHILE)
// goto Sys.init
@Sys.init$WHILE
0;JMP        
