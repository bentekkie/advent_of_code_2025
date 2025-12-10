#!/usr/bin/env python

inp = "input.txt"
games = []
with open(inp, "r") as f:
    for line in f:
        parts = line.strip().split(" ")
        want = tuple(x == "#" for x in parts[0][1:-1])
        buttons = [{int(x) for x in btn[1:-1].split(",")} for btn in parts[1:-1]]
        games.append((want, buttons))


def applybtn(st, btn):
    return tuple(not x if i in btn else x for i, x in enumerate(st))


def play(want, buttons):
    start = tuple(False for _ in want)
    seen = set()
    tocheck = {start}
    it = 0
    while True:
        it += 1
        newcheck = set()
        for ch in tocheck:
            if ch in seen:
                continue
            seen.add(ch)
            for btn in buttons:
                n = applybtn(ch, btn)
                if n == want:
                    return it
                newcheck.add(n)
        tocheck = newcheck


print("part0", sum(play(*game) for game in games))
