
load overflow.asm,
output-file overflow.out,
compare-to overflow.cmp,
output-list RAM[256]%D1.6.1 
RAM[257]%D1.6.1 RAM[258]%D1.6.1 RAM[259]%D1.6.1 
RAM[260]%D1.6.1 RAM[261]%D1.6.1 RAM[262]%D1.6.1 
RAM[263]%D1.6.1 RAM[264]%D1.6.1 RAM[265]%D1.6.1 
RAM[266]%D1.6.1 RAM[267]%D1.6.1 RAM[268]%D1.6.1 
RAM[269]%D1.6.1 RAM[270]%D1.6.1 RAM[271]%D1.6.1 
RAM[272]%D1.6.1 RAM[273]%D1.6.1 RAM[274]%D1.6.1;

set RAM[0] 256,   // initializes the stack pointer

repeat 1500 {      // enough cycles to complete the execution
  ticktock;
}

// Output the outputs of all lt, gt, eq combinations with overflow possibilities
output;
