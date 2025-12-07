#!/usr/bin/env python3

inp = "input.txt"


def ns(p):
    r, c = p
    return {
        (r, c + 1),
        (r + 1, c + 1),
        (r + 1, c),
        (r - 1, c + 1),
        (r + 1, c - 1),
        (r, c - 1),
        (r - 1, c),
        (r - 1, c - 1),
    }


with open(inp, "r") as f:
    tps = {
        (r, c)
        for r, line in enumerate(f)
        for c, x in enumerate(line.strip())
        if x == "@"
    }
orig = len(tps)
while True:
    torem = {tp for tp in tps if len(tps & ns(tp)) < 4}
    if not torem:
        break
    tps -= torem
print("part2", orig - len(tps))
