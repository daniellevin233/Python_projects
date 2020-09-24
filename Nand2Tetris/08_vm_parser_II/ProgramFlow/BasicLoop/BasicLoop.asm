//
@0
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
// set current memory index for pop
@0 // calc address
D=A
@LCL
A=M+D
D=A
@R13
M=D
// pop {0} {1} 
@SP
M=M-1
A=M
D=M
@R13
A=M // goto MEMSEG i
M=D
(LOOP_START)
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
// set current memory index for push
@0 // calc address
D=A
@LCL
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
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
// set current memory index for pop
@0 // calc address
D=A
@LCL
A=M+D
D=A
@R13
M=D
// pop {0} {1} 
@SP
M=M-1
A=M
D=M
@R13
A=M // goto MEMSEG i
M=D
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
// set current memory index for pop
@0 // calc address
D=A
@ARG
A=M+D
D=A
@R13
M=D
// pop {0} {1} 
@SP
M=M-1
A=M
D=M
@R13
A=M // goto MEMSEG i
M=D
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
// if-goto LOOP_START 
@SP // pop the topmost value from the stack
M=M-1
A=M
D=M
@LOOP_START
D;JNE
// set current memory index for push
@0 // calc address
D=A
@LCL
D=M+D
A=D
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
