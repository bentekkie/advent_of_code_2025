#!/usr/bin/env python3
res = 0
dial = 50
with open("input.txt") as f:
	for line in f.readlines():
		c,n = line[0], int(line[1:])
		full = n//100
		res += full
		n -= full*100
		if n == 0:
			continue
		z = dial != 0
		if c == "L":
			dial -= n
			if dial <= 0 and z:
				res += 1
			dial %= 100
		elif c == "R":
			dial += n
			if dial >= 100 and z:
				res += 1
			dial %= 100

print(res)
