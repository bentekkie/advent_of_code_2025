#!/usr/bin/env python3
from itertools import combinations

inp = "input.txt"

with open(inp, "r") as f:
    pnts = tuple(tuple(int(x) for x in line.strip().split(",")) for line in f)

l = 0


def inthebox(a, b):
    xmin, xmax = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
    ymin, ymax = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])
    return any(
        (
            ymin < pnts[i][1] < ymax
            and (
                xmin < pnts[i][0] < xmax
                or (pnts[i - 1][0] <= xmin and pnts[i][0] >= xmax)
                or (pnts[i][0] <= xmin and pnts[i - 1][0] >= xmax)
            )
        )
        or (
            xmin < pnts[i][0] < xmax
            and (
                ymin < pnts[i][1] < ymax
                or (pnts[i - 1][1] <= ymin and pnts[i][1] >= ymax)
                or (pnts[i][1] <= ymin and pnts[i - 1][1] >= ymax)
            )
        )
        for i in range(len(pnts))
        if pnts[i] != a and pnts[i] != b
    )


l = max(
    (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))
    for a, b in combinations(pnts, 2)
    if not inthebox(a, b)
)
print("part2", l)
