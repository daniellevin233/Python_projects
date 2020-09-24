// File name: projects/04/Divide.asm

	@quotient
	M=0
	
	@R13
	D=M
	@R14
	D=D-M
	@END
	D;JLT // if dividend < divisor, return 0
	
	@R13
	D=M
	@dividend
	M=D
	@dividend_MSB
	M=D

	@R14
	D=M
	@divisor
	M=D
	@divisor_MSB
	M=D

	@dividend_MSB_position
	M=0

	@divisor_MSB_position
	M=0

(DIVIDEND_MSB_POSITION_LOOP) // count number of bits before MBS of dividend
	@dividend_MSB
	D=M
	@DIVISOR_MSB_POSITION_LOOP
	D;JEQ

	@dividend_MSB_position
	M=M+1

	@dividend_MSB
	M=M>>
    
	@DIVIDEND_MSB_POSITION_LOOP
	0;JMP

(DIVISOR_MSB_POSITION_LOOP) // count number of bits before MBS of divisor
	@divisor_MSB
	D=M
	@DIFF_SET_LOOP
	D;JEQ

	@divisor_MSB_position
	M=M+1

	@divisor_MSB
	M=M>>

	@DIVISOR_MSB_POSITION_LOOP
	0;JMP

(DIFF_SET_LOOP) // set integer number for difference of number of bits between MSBs of dividend and divisor
	@dividend_MSB_position
	D=M
	@divisor_MSB_position
	D=D-M
	@bit_diff
	M=D
	@bit_diff_another
	M=D

(ALIGN_LOOP) // align dividend and divisor according to their MSB
	@bit_diff
	D=M
	@DIVISION_LOOP
	D;JEQ

	@bit_diff
	M=M-1

	@divisor
	M=M<<

	@ALIGN_LOOP
	0;JMP

(DIVISION_LOOP)
    @bit_diff_another
	D=M+1
	@END
	D;JEQ
	
	@bit_diff_another
	M=M-1
	
	@quotient
	M=M<<
	
	@dividend
	D=M
	@divisor
	D=D-M // cur_dividend - cur_divisor
	
	@CUR_QUOTIENT_BIT_ONE
	D;JGE // jump to the bigger loop with assigning 1 to current quotient bit iff divisor < dividend
	
	@divisor
	M=M>> // otherwise apply shiftleft on quotient without changing its last bit
	
	@DIVISION_LOOP
	0;JMP
	
(CUR_QUOTIENT_BIT_ONE)
	@divisor
	D=M
	@dividend
	M=M-D
	
	@quotient
	M=M+1
	
	@divisor
	M=M>>
	
	@DIVISION_LOOP
	0;JMP
	
(END)
	@quotient
	D=M
	@R15
	M=D
