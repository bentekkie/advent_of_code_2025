#!/usr/bin/env python3
from collections import defaultdict

inp = "input.txt"

sps = defaultdict(list)
lastcol = 0
with open(inp, "r") as f:
    for row, line in enumerate(f):
        for col, c in enumerate(line.strip()):
            if c == "^":
                sps[row].append(col)
            if c == "S":
                start = (col, row)
            lastcol = max(lastcol, col)

cnts = [0 for _ in range(lastcol + 1)]
cnts[start[0]] = 1
for crow in range(1, lastrow + 1):
    newcnts = cnts[:]
    for spc in sps[crow]:
        newcnts[spc - 1] += newcnts[spc]
        newcnts[spc + 1] += newcnts[spc]
        newcnts[spc] = 0
    cnts = newcnts

print("part1", sum(newcnts))
