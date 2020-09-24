// function SimpleFunction.test 2 
(SimpleFunction.test)
@2
D=A
(SimpleFunction.test$PUSH_LOOP) // SimpleFunction.test
@SimpleFunction.test$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@SimpleFunction.test$PUSH_LOOP
0;JMP
(SimpleFunction.test$END)
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
// set current memory index for push
@1 // calc address
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
// not
// neg
@SP // pop number
M=M-1
A=M
D=M
@R15
MD=!D
@SP // push result
A=M
M=D
@SP
M=M+1
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
@1 // calc address
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
// return 
@LCL
D=M
@frame // frame temporary variable
M=D
@5
A=D-A
D=M
@ret_address // return-address temporary variable
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
@frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@frame
A=M-D
D=M
@LCL
M=D
@ret_address // goto the return-address
A=M
0;JMP
