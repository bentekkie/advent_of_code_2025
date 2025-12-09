#!/usr/bin/env python3
from itertools import combinations
from shapely import LinearRing, box, Polygon

inp = "input.txt"

with open(inp, "r") as f:
    pnts = [tuple(int(x) for x in line.strip().split(",")) for line in f]
ring = Polygon(LinearRing(pnts))

l = 0
for (ax, ay), (bx, by) in combinations(pnts, 2):
    xmin, xmax = min(ax, bx), max(ax, bx)
    ymin, ymax = min(ay, by), max(ay, by)
    b = box(xmin, ymin, xmax, ymax)
    if ring.contains(b):
        l = max((1 + abs(ax - bx)) * (1 + abs(ay - by)), l)

print("part2", l)
