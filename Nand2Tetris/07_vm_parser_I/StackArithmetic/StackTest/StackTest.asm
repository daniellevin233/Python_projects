// push constant 17
@17
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@0
A=A+D
D=A
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
// eq
(GOOD_INPUT_1)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_1
D;JEQ
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
// push constant 17
@17
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_2
D;JEQ
@R14
D=M
@GOOD_INPUT_2
D;JEQ
(BAD_INPUT_2) // check sign of first num
@R13
D=M
@NEG_2
D;JLT
@POS_2
0;JMP
(NEG_2) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_2 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_2
0;JMP
(POS_2) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_2 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_2
0;JMP
(MAKE_VALUE_ZERO_2)
@R14 // Make second num zero
M=0
// eq
(GOOD_INPUT_2)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_2
D;JEQ
(FALSE_2)
@R15
M=0
(END_2)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 16
@16
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 17
@17
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_3
D;JEQ
@R14
D=M
@GOOD_INPUT_3
D;JEQ
(BAD_INPUT_3) // check sign of first num
@R13
D=M
@NEG_3
D;JLT
@POS_3
0;JMP
(NEG_3) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_3 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_3
0;JMP
(POS_3) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_3 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_3
0;JMP
(MAKE_VALUE_ZERO_3)
@R14 // Make second num zero
M=0
// eq
(GOOD_INPUT_3)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_3
D;JEQ
(FALSE_3)
@R15
M=0
(END_3)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_4
D;JEQ
@R14
D=M
@GOOD_INPUT_4
D;JEQ
(BAD_INPUT_4) // check sign of first num
@R13
D=M
@NEG_4
D;JLT
@POS_4
0;JMP
(NEG_4) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_4 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_4
0;JMP
(POS_4) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_4 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_4
0;JMP
(MAKE_VALUE_ZERO_4)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_4)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_4
D;JLT
(FALSE_4)
@R15
M=0
(END_4)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 892
@892
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_5
D;JEQ
@R14
D=M
@GOOD_INPUT_5
D;JEQ
(BAD_INPUT_5) // check sign of first num
@R13
D=M
@NEG_5
D;JLT
@POS_5
0;JMP
(NEG_5) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_5 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_5
0;JMP
(POS_5) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_5 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_5
0;JMP
(MAKE_VALUE_ZERO_5)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_5)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_5
D;JLT
(FALSE_5)
@R15
M=0
(END_5)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 891
@891
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_6
D;JEQ
@R14
D=M
@GOOD_INPUT_6
D;JEQ
(BAD_INPUT_6) // check sign of first num
@R13
D=M
@NEG_6
D;JLT
@POS_6
0;JMP
(NEG_6) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_6 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_6
0;JMP
(POS_6) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_6 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_6
0;JMP
(MAKE_VALUE_ZERO_6)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_6)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_6
D;JLT
(FALSE_6)
@R15
M=0
(END_6)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_7
D;JEQ
@R14
D=M
@GOOD_INPUT_7
D;JEQ
(BAD_INPUT_7) // check sign of first num
@R13
D=M
@NEG_7
D;JLT
@POS_7
0;JMP
(NEG_7) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_7 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_7
0;JMP
(POS_7) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_7 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_7
0;JMP
(MAKE_VALUE_ZERO_7)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_7)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_7
D;JGT
(FALSE_7)
@R15
M=0
(END_7)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32767
@32767
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_8
D;JEQ
@R14
D=M
@GOOD_INPUT_8
D;JEQ
(BAD_INPUT_8) // check sign of first num
@R13
D=M
@NEG_8
D;JLT
@POS_8
0;JMP
(NEG_8) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_8 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_8
0;JMP
(POS_8) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_8 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_8
0;JMP
(MAKE_VALUE_ZERO_8)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_8)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_8
D;JGT
(FALSE_8)
@R15
M=0
(END_8)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 32766
@32766
D=A
@0
A=A+D
D=A
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
@GOOD_INPUT_9
D;JEQ
@R14
D=M
@GOOD_INPUT_9
D;JEQ
(BAD_INPUT_9) // check sign of first num
@R13
D=M
@NEG_9
D;JLT
@POS_9
0;JMP
(NEG_9) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_9 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_9
0;JMP
(POS_9) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_9 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_9
0;JMP
(MAKE_VALUE_ZERO_9)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_9)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_9
D;JGT
(FALSE_9)
@R15
M=0
(END_9)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 57
@57
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 31
@31
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 53
@53
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
// push constant 112
@112
D=A
@0
A=A+D
D=A
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
// neg
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
// and
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
MD=D&M
@SP // push result
A=M
M=D
@SP
M=M+1
// push constant 82
@82
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
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
MD=D|M
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
