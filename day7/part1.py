#!/usr/bin/env python3
from collections import defaultdict

inp = "input.txt"


bms = defaultdict(bool)
s = 0
with open(inp, "r") as f:
    for line in f:
        for col, c in enumerate(line.strip()):
            if c == "^" and bms[col]:
                s += 1
                bms[col] = False
                bms[col - 1] = True
                bms[col + 1] = True
            if c == "S":
                bms[col] = True

print("part1", s)
