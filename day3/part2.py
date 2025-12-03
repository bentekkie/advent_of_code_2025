#!/usr/bin/env python3

inp = "input.txt"

with open(inp,"r") as f:
	banks = [[int(x) for x in line.strip()] for line in f]

s = 0
for bank in banks:
  prev = [0 for _ in range(13)]
  for x in bank:
    prev = [max(prev[idx], prev[idx-1]*10+x) if idx > 0 else prev[idx] for idx in range(13)]
  s += prev[-1]
print('part 2', s)
