#!/usr/bin/env bash
# Compares my assembler's output with the official Assembler for the 4 test programs.
# Run from the capstone/ folder:   sh check_assembler.sh
cd "$(dirname "$0")"
TMP=$(mktemp -d)
for p in Add Max Rect Pong Box; do
    if [ "$p" = "Box" ]; then src=Box.asm; else src=asm_tests/$p.asm; fi
    cp "$src" "$TMP/$p.asm"
    ../tools/Assembler.sh "$TMP/$p.asm" >/dev/null 2>&1          # official -> $TMP/$p.hack
    python3 assembler.py "$src" "$TMP/mine_$p.hack" >/dev/null   # mine
    if diff -q <(tr -d '\r' < "$TMP/$p.hack") "$TMP/mine_$p.hack" >/dev/null; then
        echo "$p: my assembler == official assembler"
    else
        echo "$p: DIFFERENT"
    fi
done
rm -rf "$TMP"
