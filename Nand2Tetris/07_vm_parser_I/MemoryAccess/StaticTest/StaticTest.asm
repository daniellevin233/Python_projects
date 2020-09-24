//
@111
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
//
@333
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
//
@888
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
//
@StaticTest.8
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
//
@StaticTest.3
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
//
@StaticTest.1
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
//
@StaticTest.3
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@StaticTest.1
D=M
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
//
@StaticTest.8
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
