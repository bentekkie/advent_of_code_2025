#!/usr/bin/env python3
from collections import defaultdict

inp = "input.txt"

cnts = defaultdict(int)
with open(inp, "r") as f:
    for row, line in enumerate(f):
        for col, c in enumerate(line.strip()):
            if c == "^":
                cnts[col - 1] += cnts[col]
                cnts[col + 1] += cnts[col]
                del cnts[col]
            if c == "S":
                cnts[col] = 1
print("part1", sum(cnts.values()))
