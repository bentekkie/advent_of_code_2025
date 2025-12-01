#!/usr/bin/python3

res = 0
dial = 50
with open("input.txt") as f:
	for line in f.readlines():
		n = int(line[1:])
		full = n//100
		res += full
		n -= full*100
		if n == 0:
			continue
		atz = dial == 0
		if line[0] == "L":
			dial = (dial - n)
			if dial < 0 and not atz:
				res += 1
			dial %= 100
		elif line[0] == "R":
			dial = (dial + n)
			if dial > 100 and not atz:
				res += 1
			dial %= 100
		if dial == 0:
			res += 1
		#print(line.strip(), dial, res)

print(res)
