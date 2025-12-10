#!/usr/bin/env python
from scipy.optimize import linprog

inp = "input.txt"
s = 0
with open(inp, "r") as f:
    for line in f:
        parts = line.strip().split(" ")
        want = tuple(int(x) for x in parts[-1][1:-1].split(","))
        buttons = [{int(x) for x in btn[1:-1].split(",")} for btn in parts[1:-1]]
        s += sum(
            linprog(
                [1] * len(buttons),
                A_eq=[[int(i in btn) for btn in buttons] for i, w in enumerate(want)],
                b_eq=want,
                integrality=[1] * len(buttons),
            ).x
        )


print("part1", s)
