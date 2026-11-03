// Step 2 - wider dash: paint 4 words (64 pixels) of row 43 with a loop.
    @SCREEN
    D=A
    @1376
    D=D+A
    @ptr
    M=D             // ptr = 17760 (first word of row 43)
    @4
    D=A
    @cols
    M=D             // cols = 4 words to paint
(WORD)
    @ptr
    A=M
    M=-1            // RAM[ptr] = -1 (black)
    @ptr
    M=M+1           // ptr = ptr + 1
    @cols
    MD=M-1          // cols = cols - 1
    @WORD
    D;JGT           // repeat while cols > 0
(END)
    @END
    0;JMP
