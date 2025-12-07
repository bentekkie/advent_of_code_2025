#!/usr/bin/env python3

inp = "input.txt"

ranges = []
with open(inp, "r") as f:
    for line in f:
        if line.strip() == "":
            break
        l, r = line.strip().split("-")
        ranges.append((int(l), int(r)))
    ids = [int(line.strip()) for line in f]
s = sum(1 for id in ids if any(l <= id <= r for l, r in ranges))

print("part", s)
