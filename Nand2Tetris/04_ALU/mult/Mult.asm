// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	// zero register of the result
	@R2
	MD=0

	// declare variables
	@R0
	D=M
	@incstep
	M=D

	// check whether the first input is zero
	@ZERO
	D;JEQ

	@R1
	D=M
	@times
	M=D

	// check whether the second input is zero
	@ZERO
	D;JEQ

(LOOP)
	@incstep
	D=M
	@R2
	M=M+D
	@times
	MD=M-1
	@LOOP
	D;JGT // if times > 0 keep looping, else leave the loop

(ZERO)
