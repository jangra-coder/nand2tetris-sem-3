# Capstone - Make the Computer Draw a Box

Rahul, 2501350043

K = 43

- K mod 3 = 1, so my assembler shows the line number when a line is wrong
- K mod 4 = 3, so the box is 16 x 4 = 64 pixels wide
- box starts at row 43 and is 20 rows tall (row 43 to 62)

## Files

- `CPU.hdl`, `Memory.hdl`, `Computer.hdl` - Part A
- other .hdl files - my chips from the labs (gates, adders, ALU)
- .tst / .cmp files and `Add.hack`, `Max.hack`, `Rect.hack` - official test files for Part A
- `assembler.py` - Part B
- `asm_tests/` - Add, Max, Rect and Pong programs I used to test the assembler
- `Box.asm`, `Box.hack` - Part C (Box.hack is made with my assembler)

PC and RAM16K are the built-in chips here. The Computer test files read `PC[]` and `RAM16K[0]` directly and that only works with built-in chips. My own PC and RAM16K are in `projects/03` and pass their tests there.

## How to run

Part A - open `CPU.tst` in the Hardware Simulator and run it. Same for `Memory.tst`, `ComputerAdd.tst`, `ComputerMax.tst` and `ComputerRect.tst`.

Part B - `python3 assembler.py asm_tests/Pong.asm` (makes Pong.hack next to it)

Part C - `python3 assembler.py Box.asm`, then load `Box.hack` in the CPU Emulator, run it and hold any key.
