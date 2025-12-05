#!/usr/bin/env python3

inp = "input.txt"

ranges = []
with open(inp,"r") as f:
	for line in f:
		if line.strip() == "":
			break
		l,r = line.strip().split("-")
		ranges.append((int(l),int(r)))
	ids = [int(line.strip()) for line in f]

ranges.sort()


i = 0
s = 0
while i < len(ranges):
	l,r = ranges[i]
	#print(l,r)
	while i+1 < len(ranges) and r >= ranges[i+1][0]:
		#print("add", ranges[i+1])
		_,newr=ranges[i+1]
		r= max(r,newr)
		i+=1
	#print(l,r)
	s+=r-l+1
	i+=1
print('part2',s)
