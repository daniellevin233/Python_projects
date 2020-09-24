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
// function Class1.set 0 
(Class1.set)
@0
D=A
(Class1.set$PUSH_LOOP) // SimpleFunction.test
@Class1.set$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Class1.set$PUSH_LOOP
0;JMP
(Class1.set$END)
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
@Class1.0
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
//
@Class1.1
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
// return 
@LCL
D=M
@Class1.set$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Class1.set$ret_address // return-address temporary variable
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
@Class1.set$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Class1.set$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Class1.set$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Class1.set$frame
A=M-D
D=M
@LCL
M=D
@Class1.set$ret_address // goto the return-address
A=M
0;JMP
// function Class1.get 0 
(Class1.get)
@0
D=A
(Class1.get$PUSH_LOOP) // SimpleFunction.test
@Class1.get$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Class1.get$PUSH_LOOP
0;JMP
(Class1.get$END)
//
@Class1.0
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@Class1.1
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
@Class1.get$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Class1.get$ret_address // return-address temporary variable
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
@Class1.get$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Class1.get$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Class1.get$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Class1.get$frame
A=M-D
D=M
@LCL
M=D
@Class1.get$ret_address // goto the return-address
A=M
0;JMP
// function Class2.set 0 
(Class2.set)
@0
D=A
(Class2.set$PUSH_LOOP) // SimpleFunction.test
@Class2.set$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Class2.set$PUSH_LOOP
0;JMP
(Class2.set$END)
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
@Class2.0
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
//
@Class2.1
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
// return 
@LCL
D=M
@Class2.set$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Class2.set$ret_address // return-address temporary variable
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
@Class2.set$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Class2.set$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Class2.set$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Class2.set$frame
A=M-D
D=M
@LCL
M=D
@Class2.set$ret_address // goto the return-address
A=M
0;JMP
// function Class2.get 0 
(Class2.get)
@0
D=A
(Class2.get$PUSH_LOOP) // SimpleFunction.test
@Class2.get$END
D;JEQ
@SP // push 0
A=M
M=0
@SP
M=M+1
D=D-1
@Class2.get$PUSH_LOOP
0;JMP
(Class2.get$END)
//
@Class2.0
D=M
// push
@SP
A=M
M=D
@SP
M=M+1
//
@Class2.1
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
@Class2.get$frame // frame temporary variable
M=D
@5
A=D-A
D=M
@Class2.get$ret_address // return-address temporary variable
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
@Class2.get$frame // restore THAT
A=M-1
D=M
@THAT
M=D
@2 // restore THIS
D=A
@Class2.get$frame
A=M-D
D=M
@THIS
M=D
@3 // restore ARG
D=A
@Class2.get$frame
A=M-D
D=M
@ARG
M=D
@4 // restore LCL
D=A
@Class2.get$frame
A=M-D
D=M
@LCL
M=D
@Class2.get$ret_address // goto the return-address
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
//
@8
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
// call Class1.set 2 
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
@2
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Class1.set // goto function
0;JMP 
(Sys.init$ret.0)
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
//
@23
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
@15
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
// call Class2.set 2 
@Sys.init$ret.1 // push return address
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
@2
D=D+A
@SP
D=M-D
@ARG
M=D
@SP // LCL = SP
D=M
@LCL
M=D
@Class2.set // goto function
0;JMP 
(Sys.init$ret.1)
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
// call Class1.get 0 
@Sys.init$ret.2 // push return address
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
@Class1.get // goto function
0;JMP 
(Sys.init$ret.2)
// call Class2.get 0 
@Sys.init$ret.3 // push return address
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
@Class2.get // goto function
0;JMP 
(Sys.init$ret.3)
(Sys.init$WHILE)
// goto Sys.init
@Sys.init$WHILE
0;JMP        
