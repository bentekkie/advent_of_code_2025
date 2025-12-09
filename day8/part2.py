#!/usr/bin/env python3
from itertools import combinations
from math import sqrt

inp = "input.txt"


def dist(p1, p2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


with open(inp, "r") as f:
    coords = [tuple(int(x) for x in line.strip().split(",")) for line in f]


pairs = sorted(((a, b) for a, b in combinations(coords, 2)), key=lambda x: dist(*x))

cir = {i: [coord] for i, coord in enumerate(coords)}
cc = {coord: i for i, coord in enumerate(coords)}
for a, b in pairs:
    if cc[a] == cc[b]:
        continue
    ca, cb = cc[a], cc[b]
    cir[ca] += cir[cb]
    for c in cir[cb]:
        cc[c] = ca
    del cir[cb]
    if len(cir) == 1:
        break
print("part2", a[0] * b[0])
