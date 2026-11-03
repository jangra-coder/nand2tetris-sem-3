# Capstone Project - Make the Computer Draw a Box

Rahul (2501350043)

Nand to Tetris - I (ETCCNT301)

## My K

K = last two digits of roll number = **43**

- K mod 3 = 1  -> extra assembler feature: show a clear error message with the line number
- K mod 4 = 3  -> box width = 16 x (3 + 1) = 64 pixels (4 words)
- Box starts at row 43 and is 20 rows tall (rows 43 to 62)
- First address of the box = SCREEN + 32 x 43 = 16384 + 1376 = 17760

## Files

```
CPU.hdl, Memory.hdl, Computer.hdl   -> Part A (the Hack computer)
other .hdl files                    -> my lab chips (gates, ALU, PC, Register, Bit) used by the CPU
*.tst, *.cmp, *.hack                -> official test files for Part A
assembler.py                        -> Part B (Hack assembler in Python)
asm_tests/                          -> Add, Max, Rect, Pong programs used to test the assembler
asm_tests/official/                 -> output of the official Nand2Tetris assembler for the same programs
check_assembler.sh                  -> compares my assembler output with the official assembler
Box.asm                             -> Part C (box program)
Box.hack                            -> Box.asm converted using my assembler
steps/                              -> how I built Box.asm step by step (dash -> wide dash -> box)
```

## How to Run

### Part A

Open the Hardware Simulator, load `CPU.tst` and run it. Same for `Memory.tst`,
`ComputerAdd.tst`, `ComputerMax.tst` and `ComputerRect.tst`.

The RAM16K, Screen and Keyboard inside Memory use the built-in chips of the simulator
(my RAM16K made from registers is too slow to simulate), all other chips are mine.

### Part B

```
python3 assembler.py asm_tests/Pong.asm
```

This makes `asm_tests/Pong.hack`. To compare my output with the official assembler output
(saved in `asm_tests/official/`):

```
bash check_assembler.sh
```

If there is a wrong line in the .asm file, the assembler does not crash. It shows the line number:

```
Line 7: invalid instruction - unknown computation 'Q'
No .hack file was written.
```

### Part C

```
python3 assembler.py Box.asm
```

Then open the CPU Emulator, load `Box.hack`, select View -> Screen, run it and hold any key.
The box comes at rows 43 to 62 on the left side. When the key is released the box goes away.
