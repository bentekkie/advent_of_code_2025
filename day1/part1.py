#!/usr/bin/python3

res = 0
dial = 50
with open("input.txt") as f:
	for line in f.readlines():
		if line[0] == "L":
			dial = (dial - int(line[1:]))% 100
		elif line[0] == "R":
			dial = (dial + int(line[1:]))%100
		if dial == 0:
			res += 1

print(res)
