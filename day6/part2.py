#!/usr/bin/env python3
from operator import mul, add
from functools import reduce
import re

inp = "input.txt"

with open(inp, "r") as f:
    lines = [line.replace("\n", "") + " " for line in f]

syms = lines[-1]
parts = [len(s) for s in re.findall(r"[\*\+] +", syms)]
st = 0
s = 0
for p in parts:
    s += reduce(
        add if "+" in syms[st : st + p] else mul,
        (
            int("".join(n).strip())
            for n in zip(*(l[st : st + p - 1] for l in lines[:-1]))
        ),
    )
    st += p
print("part2", s)
