#!/usr/bin/env python3
from operator import mul
from functools import reduce

inp = "input.txt"

with open(inp, "r") as f:
    lines = [line.split() for line in f]
s = 0
for sym, *nums in zip(*lines[::-1]):
    if sym == "+":
        s += sum(int(x) for x in nums)
    if sym == "*":
        s += reduce(mul, (int(x) for x in nums))
print("part1", s)
