#!/usr/bin/env python3

inp = "input.txt"

with open(inp,"r") as f:
	banks = [[int(x) for x in line.strip()] for line in f]

s = 0
for bank in banks:
  n, prevIdx = 0, len(bank)
  for i in range(12):
    n, prevIdx = max((n*10+x, 11-i+k) for k, x in enumerate(bank[len(bank)-prevIdx:len(bank)-11+i][::-1]))
  s += n
print('part 2', s)