#!/usr/bin/env python3

inp = "input.txt"

sps = set()
lastcol = 0
with open(inp, "r") as f:
    for row, line in enumerate(f):
        for col, c in enumerate(line.strip()):
            if c == "^":
                sps.add((col, row))
            if c == "S":
                start = (col, row)
            lastcol = max(lastcol, col)
lastrow = row

seensps = set()
seen = set()
check = {start}
while len(check) > 0:
    newcheck = set()
    for ch in check:
        seen.add(ch)
        chcol, chrow = ch
        if ch in sps:
            seensps.add(ch)
            l, r = (chcol - 1, chrow), (chcol + 1, chrow)
            if l not in seen and chcol > 0:
                newcheck.add(l)
            if r not in seen and chcol < lastcol:
                newcheck.add(r)
        elif chrow < lastrow:
            newcheck.add((chcol, chrow + 1))
    check = newcheck

print("part1", len(seensps))
