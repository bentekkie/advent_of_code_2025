#!/usr/bin/env python3
from itertools import combinations
from math import sqrt

inp = "input.txt"


def dist(p1, p2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


with open(inp, "r") as f:
    coords = [tuple(int(x) for x in line.strip().split(",")) for line in f]


pairs = sorted((dist(a, b), a, b) for a, b in combinations(coords, 2))

cir = {i: {coord} for i, coord in enumerate(coords)}
cc = {coord: i for i, coord in enumerate(coords)}
for _, a, b in pairs[:1000]:
    if cc[a] == cc[b]:
        continue
    n = min(cc[a], cc[b])
    nc = cir[cc[a]] | cir[cc[b]]
    del cir[cc[a]]
    del cir[cc[b]]
    cir[n] = nc
    for c in nc:
        cc[c] = n
lens = sorted((len(g) for i, g in cir.items()), reverse=True)
print("part1", lens[0] * lens[1] * lens[2])
