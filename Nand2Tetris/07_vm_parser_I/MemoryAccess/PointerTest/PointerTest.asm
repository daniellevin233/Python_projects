//
@3030
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
// access this or that content for pop
@THIS
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
@3040
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
// access this or that content for pop
@THAT
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
@32
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
@2 // calc address
D=A
@THIS
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
//
@46
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
@6 // calc address
D=A
@THAT
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
// access this or that content for push
@THIS
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
// access this or that content for push
@THAT
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
// set current memory index for push
@2 // calc address
D=A
@THIS
D=M+D
A=D
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
// set current memory index for push
@6 // calc address
D=A
@THAT
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
