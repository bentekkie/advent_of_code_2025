#!/usr/bin/env python3
inp = "input.txt"

with open(inp,"r") as f:
	banks = [[int(x) for x in line.strip()] for line in f]

s=0
for bank in banks:
	first = max((x, len(bank)-1-i) for i, x in enumerate(bank[:-1]))
	print(first)
	second = max(bank[len(bank)-first[1]:])
	n = first[0]*10+second
	print(n)
	s+=n
print('part1', s)
