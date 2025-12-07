#!/usr/bin/env python3
res = 0
dial = 50
with open("input.txt") as f:
    for line in f.readlines():
        dial = (dial + int(line[1:]) * (1 if line[0] == "R" else -1)) % 100
        if not dial:
            res += 1

print(res)
