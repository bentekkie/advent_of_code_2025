#!/usr/bin/env python3
from itertools import combinations

inp = "input.txt"

with open(inp, "r") as f:
    pnts = [tuple(int(x) for x in line.strip().split(",")) for line in f]

l = 0


def inthebox(ax, ay, bx, by):
    xmin, xmax = min(ax, bx), max(ax, bx)
    ymin, ymax = min(ay, by), max(ay, by)
    return any(
        (xmin < px < xmax and ymin < py < ymax)
        or (
            ymin < py < ymax
            and (
                (pnts[i - 1][0] <= xmin and px >= xmax)
                or (px <= xmin and pnts[i - 1][0] >= xmax)
            )
        )
        or (
            xmin < px < xmax
            and (
                (pnts[i - 1][1] <= ymin and py >= ymax)
                or (py <= ymin and pnts[i - 1][1] >= ymax)
            )
        )
        for i, (px, py) in enumerate(pnts)
        if (px, py) != (ax, ay) and (px, py) != (bx, by)
    )

    return False


for (ax, ay), (bx, by) in combinations(pnts, 2):
    s = (1 + abs(ax - bx)) * (1 + abs(ay - by))
    if inthebox(ax, ay, bx, by):
        continue
    if s > l:
        l = s
print("part2", l)
