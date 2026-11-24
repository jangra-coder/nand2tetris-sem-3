# Hack Assembler - Capstone Part B
# Rahul, Roll no. 2501350043, K = 43
#
# K mod 3 = 1, so my extra feature is: if a line is wrong, print the
# line number and the problem (for example "Line 7: invalid instruction")
# and stop, instead of crashing with a python error.
#
# How to run:   python3 assembler.py Add.asm
# It makes Add.hack in the same folder.

import sys

# comp part -> 7 bits (a c1 c2 c3 c4 c5 c6)
comp_table = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "!D": "0001101",
    "!A": "0110001", "-D": "0001111", "-A": "0110011",
    "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M": "1110000", "!M": "1110001", "-M": "1110011",
    "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
    "D|M": "1010101",
}

# dest part -> 3 bits (A D M)
dest_table = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111",
}

# jump part -> 3 bits (j1 j2 j3)
jump_table = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}

# symbols that are already defined in every hack program
symbols = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
}
for i in range(16):
    symbols["R" + str(i)] = i


def error(line_no, message):
    # my K feature: show the line number and stop the program nicely
    print(f"Line {line_no}: invalid instruction - {message}")
    print("No .hack file was made.")
    sys.exit(1)


def clean(line):
    # remove the comment and all the spaces from a line
    if "//" in line:
        line = line[:line.index("//")]
    line = line.replace(" ", "").replace("\t", "")
    return line.strip()


def is_symbol(name):
    # a symbol can have letters, digits, _ . $ : but cannot start with a digit
    if name == "" or name[0].isdigit():
        return False
    for ch in name:
        if not (ch.isalnum() or ch in "_.$:"):
            return False
    return True


# ---------------- read the .asm file ----------------
if len(sys.argv) != 2 or not sys.argv[1].endswith(".asm"):
    print("Usage: python3 assembler.py Prog.asm")
    sys.exit(1)

asm_file = sys.argv[1]
hack_file = asm_file[:-4] + ".hack"

# keep only the real instructions, together with their line number
lines = []
f = open(asm_file)
line_no = 0
for raw_line in f:
    line_no += 1
    text = clean(raw_line)
    if text != "":
        lines.append((line_no, text))
f.close()


# ---------------- first pass: find the labels ----------------
# a label like (LOOP) is not an instruction, it is just the
# address of the next instruction, so only count real instructions
rom_address = 0
for line_no, text in lines:
    if text[0] == "(":
        name = text[1:-1]
        if text[-1] != ")" or not is_symbol(name):
            error(line_no, "wrong label " + text)
        symbols[name] = rom_address
    else:
        rom_address += 1

# ---------------- second pass: make the 16 bit codes ----------------
output = []
next_variable = 16      # new variables go to RAM 16, 17, 18 ...

for line_no, text in lines:
    if text[0] == "(":
        continue        # labels were done in the first pass

    if text[0] == "@":
        # A-instruction:  0 + value in 15 bits
        value = text[1:]
        if value.isdigit():
            number = int(value)
            if number > 32767:
                error(line_no, "number is too big " + value)
        elif is_symbol(value):
            if value not in symbols:
                symbols[value] = next_variable
                next_variable += 1
            number = symbols[value]
        else:
            error(line_no, "wrong value after @: " + value)
        output.append("0" + format(number, "015b"))

    else:
        # C-instruction:  dest=comp;jump  ->  111 + comp + dest + jump
        dest = ""
        jump = ""
        comp = text
        if "=" in comp:
            dest = comp.split("=")[0]
            comp = comp.split("=")[1]
        if ";" in comp:
            jump = comp.split(";")[1]
            comp = comp.split(";")[0]

        if comp not in comp_table:
            error(line_no, "unknown comp '" + comp + "'")
        if dest not in dest_table:
            error(line_no, "unknown dest '" + dest + "'")
        if jump not in jump_table:
            error(line_no, "unknown jump '" + jump + "'")
        output.append("111" + comp_table[comp] + dest_table[dest] + jump_table[jump])

# ---------------- write the .hack file ----------------
# (only reaches here if every line was correct)
f = open(hack_file, "w")
for code in output:
    f.write(code + "\n")
f.close()
print("Done:", len(output), "instructions written to", hack_file)
