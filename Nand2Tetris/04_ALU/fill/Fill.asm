// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

  @8192
  D=A
  @n
  M=D // n = 8192

(KBDLOOP)
  @SCREEN
  D=A
  @curr_word_address
  M=D // curr_word_address = 16384

  @i
  M=0 // i = 0

  @KBD
  D=M

  @color_code
  M=0 // color_code = 'white'
  @SCREENLOOP
  D;JEQ // if keyboard input is 0, then fill the screen with white

  @color_code
  M=-1 // color_code = 'black'
  @SCREENLOOP
  D;JNE // if keyboard input is different than 0, then fill the screen with black

(SCREENLOOP)
  @i
  D=M
  @n
  D=D-M
  @KBDLOOP
  D;JEQ // if i>n goto KBDLOOP

  @color_code
  D=M
  @curr_word_address
  A=M
  M=D // fill word with color

  @i
  M=M+1 // i++

  @curr_word_address
  M=M+1 // curr_word_address++

  @SCREENLOOP
  0;JMP // goto SCREENLOOP
