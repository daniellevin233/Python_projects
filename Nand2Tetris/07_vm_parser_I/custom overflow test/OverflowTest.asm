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
// push constant 1
@1
D=A
@0
A=A+D
D=A
@SP
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
// push constant 32768
@32768
D=A
@0
A=A+D
D=A
@SP
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
// push constant 1
@1
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 556
@556
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
// eq
(GOOD_INPUT_4)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_4
D;JEQ
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
// eq
(GOOD_INPUT_5)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_5
D;JEQ
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
// push constant 556
@556
D=A
@0
A=A+D
D=A
@SP
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
// eq
(GOOD_INPUT_6)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_6
D;JEQ
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
// push constant 1
@1
D=A
@0
A=A+D
D=A
@SP
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
// lt
(GOOD_INPUT_7)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_7
D;JLT
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
// push constant 32768
@32768
D=A
@0
A=A+D
D=A
@SP
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
// push constant 1
@1
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
// lt
(GOOD_INPUT_8)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_8
D;JLT
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
// push constant 554
@554
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
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
// lt
(GOOD_INPUT_9)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_9
D;JLT
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
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
@GOOD_INPUT_10
D;JEQ
@R14
D=M
@GOOD_INPUT_10
D;JEQ
(BAD_INPUT_10) // check sign of first num
@R13
D=M
@NEG_10
D;JLT
@POS_10
0;JMP
(NEG_10) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_10 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_10
0;JMP
(POS_10) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_10 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_10
0;JMP
(MAKE_VALUE_ZERO_10)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_10)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_10
D;JLT
(FALSE_10)
@R15
M=0
(END_10)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 556
@556
D=A
@0
A=A+D
D=A
@SP
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
@GOOD_INPUT_11
D;JEQ
@R14
D=M
@GOOD_INPUT_11
D;JEQ
(BAD_INPUT_11) // check sign of first num
@R13
D=M
@NEG_11
D;JLT
@POS_11
0;JMP
(NEG_11) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_11 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_11
0;JMP
(POS_11) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_11 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_11
0;JMP
(MAKE_VALUE_ZERO_11)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_11)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_11
D;JLT
(FALSE_11)
@R15
M=0
(END_11)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
@GOOD_INPUT_12
D;JEQ
@R14
D=M
@GOOD_INPUT_12
D;JEQ
(BAD_INPUT_12) // check sign of first num
@R13
D=M
@NEG_12
D;JLT
@POS_12
0;JMP
(NEG_12) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_12 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_12
0;JMP
(POS_12) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_12 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_12
0;JMP
(MAKE_VALUE_ZERO_12)
@R14 // Make second num zero
M=0
// lt
(GOOD_INPUT_12)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_12
D;JLT
(FALSE_12)
@R15
M=0
(END_12)
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
// push constant 1
@1
D=A
@0
A=A+D
D=A
@SP
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
@GOOD_INPUT_13
D;JEQ
@R14
D=M
@GOOD_INPUT_13
D;JEQ
(BAD_INPUT_13) // check sign of first num
@R13
D=M
@NEG_13
D;JLT
@POS_13
0;JMP
(NEG_13) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_13 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_13
0;JMP
(POS_13) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_13 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_13
0;JMP
(MAKE_VALUE_ZERO_13)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_13)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_13
D;JGT
(FALSE_13)
@R15
M=0
(END_13)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 32768
@32768
D=A
@0
A=A+D
D=A
@SP
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
// push constant 1
@1
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
@GOOD_INPUT_14
D;JEQ
@R14
D=M
@GOOD_INPUT_14
D;JEQ
(BAD_INPUT_14) // check sign of first num
@R13
D=M
@NEG_14
D;JLT
@POS_14
0;JMP
(NEG_14) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_14 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_14
0;JMP
(POS_14) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_14 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_14
0;JMP
(MAKE_VALUE_ZERO_14)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_14)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_14
D;JGT
(FALSE_14)
@R15
M=0
(END_14)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 554
@554
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
@GOOD_INPUT_15
D;JEQ
@R14
D=M
@GOOD_INPUT_15
D;JEQ
(BAD_INPUT_15) // check sign of first num
@R13
D=M
@NEG_15
D;JLT
@POS_15
0;JMP
(NEG_15) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_15 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_15
0;JMP
(POS_15) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_15 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_15
0;JMP
(MAKE_VALUE_ZERO_15)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_15)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_15
D;JGT
(FALSE_15)
@R15
M=0
(END_15)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
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
@GOOD_INPUT_16
D;JEQ
@R14
D=M
@GOOD_INPUT_16
D;JEQ
(BAD_INPUT_16) // check sign of first num
@R13
D=M
@NEG_16
D;JLT
@POS_16
0;JMP
(NEG_16) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_16 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_16
0;JMP
(POS_16) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_16 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_16
0;JMP
(MAKE_VALUE_ZERO_16)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_16)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_16
D;JGT
(FALSE_16)
@R15
M=0
(END_16)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 554
@554
D=A
@0
A=A+D
D=A
@SP
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
@GOOD_INPUT_17
D;JEQ
@R14
D=M
@GOOD_INPUT_17
D;JEQ
(BAD_INPUT_17) // check sign of first num
@R13
D=M
@NEG_17
D;JLT
@POS_17
0;JMP
(NEG_17) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_17 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_17
0;JMP
(POS_17) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_17 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_17
0;JMP
(MAKE_VALUE_ZERO_17)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_17)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_17
D;JGT
(FALSE_17)
@R15
M=0
(END_17)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
// push constant 555
@555
D=A
@0
A=A+D
D=A
@SP
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
@GOOD_INPUT_18
D;JEQ
@R14
D=M
@GOOD_INPUT_18
D;JEQ
(BAD_INPUT_18) // check sign of first num
@R13
D=M
@NEG_18
D;JLT
@POS_18
0;JMP
(NEG_18) // Case 1: first num neg
@R14
D=D&M
@GOOD_INPUT_18 // If both nums are negative then no need to check overflow
D;JLT
@MAKE_VALUE_ZERO_18
0;JMP
(POS_18) // Case 2: first num pos
@R14
D=D|M
@GOOD_INPUT_18 // If both nums are positive then no need to check overflow
D;JGE
@MAKE_VALUE_ZERO_18
0;JMP
(MAKE_VALUE_ZERO_18)
@R14 // Make second num zero
M=0
// gt
(GOOD_INPUT_18)
@R15
M=-1
@R13
D=M
@R14 // calc sub
MD=D-M
@END_18
D;JGT
(FALSE_18)
@R15
M=0
(END_18)
@R15 // push result
D=M
@SP
A=M
M=D
@SP
M=M+1
