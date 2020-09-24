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
@4000
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
@5000
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
// call Sys.main 0 
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
@0
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Sys.main // goto function
0;JMP 
(Sys.init$ret.0)
//
@1 // calc address
D=A
@R5
A=A+D
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
(Sys.init$LOOP)
// goto Sys.init
@Sys.init$LOOP
0;JMP        
// function Sys.main 5 
(Sys.main)
@5
D=A
(Sys.main$PUSH_LOOP) // SimpleFunction.test
@Sys.main$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Sys.main$PUSH_LOOP
0;JMP
(Sys.main$END)
//
@4001
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
@5001
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
@200
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
@1 // calc address
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
//
@40
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
//
@6
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
@3 // calc address
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
//
@123
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
// call Sys.add12 1 
@Sys.main$ret.0 // push return address
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
@Sys.add12 // goto function
0;JMP 
(Sys.main$ret.0)
//
@0 // calc address
D=A
@R5
A=A+D
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
// set current memory index for push
@2 // calc address
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
@3 // calc address
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
@4 // calc address
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
@Sys.main$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Sys.main$ret_address // return-address temporary variable
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
@Sys.main$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Sys.main$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Sys.main$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Sys.main$frame
A=M-D
D=M
@LCL
M=D
@Sys.main$ret_address // goto the return-address
A=M
0;JMP
// function Sys.add12 0 
(Sys.add12)
@0
D=A
(Sys.add12$PUSH_LOOP) // SimpleFunction.test
@Sys.add12$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Sys.add12$PUSH_LOOP
0;JMP
(Sys.add12$END)
//
@4002
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
@5002
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
@12
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
@Sys.add12$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Sys.add12$ret_address // return-address temporary variable
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
@Sys.add12$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Sys.add12$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Sys.add12$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Sys.add12$frame
A=M-D
D=M
@LCL
M=D
@Sys.add12$ret_address // goto the return-address
A=M
0;JMP
