#!/usr/bin/env python3
from itertools import combinations

inp = "input.txt"

with open(inp, "r") as f:
    pnts = [tuple(int(x) for x in line.strip().split(",")) for line in f]
l = 0
for (ax, ay), (bx, by) in combinations(pnts, 2):
    l = max((1 + abs(ax - bx)) * (1 + abs(ay - by)), l)

print("part1", l)
