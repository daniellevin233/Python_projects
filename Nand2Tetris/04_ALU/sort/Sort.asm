// File name: projects/04/Sort.asm

//

  @R14
  D=M
  @start_addr
  M=D // address of array start

  @R15
  D=M
  @size
  M=D // size

  @END
  D-1;JLE // If size < 2 then array is ordered

(OUTERLOOP)
  @i
  M=0
  @swap
  M=0 // flag that will be changed to 1 iff a swap will be made during INNERLOOP
(INNERLOOP)
  @size
  D=M-1
  @i
  D=D-M
  @END_ITER
  D;JLE // If size-i <= 1 then stop

  @start_addr
  D=M
  @i
  A=M+D // change address to array[i]
  D=A

  @first_num_addr
  M=D
  @second_num_addr
  M=D+1

  @i
  M=M+1 // i++

  @first_num_addr
  A=M
  D=M
  @second_num_addr
  A=M
  D=D-M
  @INNERLOOP
  D;JGE // if array[i] >= array[i+1], no swap is made

  // A - first num, B - second num
  // temp=B
  // B=A
  // A=temp
  @second_num_addr
  A=M
  D=M
  @temp
  M=D
  @first_num_addr
  A=M
  D=M
  @second_num_addr
  A=M
  M=D
  @temp
  D=M
  @first_num_addr
  A=M
  M=D

  @swap
  M=1 // swap flag turned on

  @INNERLOOP
  0;JMP // keep iterating in inner loop
(END_ITER)
  @swap
  D=M
  @OUTERLOOP
  D-1;JEQ // jump to outerloop iff swap was made during inner loop
(END)
