// push constant 7
@7
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 8
@8
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
// pop var 14
@SP
M=M-1
A=M
D=M
@14
D=M
@R13
A=M+D
M=D
// pop var 13
@SP
M=M-1
A=M
D=M
@13
D=M
@R13
A=M+D
M=D
@R13
D=M
@R14
D=D+M
@R15
M=D
// push var 15
@15
D=A
@R13
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
