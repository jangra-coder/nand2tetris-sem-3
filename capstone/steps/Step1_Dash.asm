// Step 1 - one dash: paint ONE word (16 pixels) black at the start of row 43.
// Address = SCREEN + 32*43 = 16384 + 1376 = 17760
    @SCREEN
    D=A
    @1376
    D=D+A           // D = 17760
    @addr
    M=D             // addr = 17760
    A=D             // A = 17760
    M=-1            // RAM[17760] = -1  -> 16 black pixels
(END)
    @END
    0;JMP           // stop here forever
