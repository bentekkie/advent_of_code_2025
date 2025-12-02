#!/usr/bin/env python3
import math
import re
with open("input.txt", "r") as f:
	ranges = [(int((p:=r.split("-"))[0]),int(p[1])) for r in f.read().strip().split(",")]
s=0
for r in ranges:
	for i in range(r[0],r[1]+1):
		#co = set()
		#d = int(math.log10(i))+1
		#if d%2 != 0:
		#	continue
		#left = (i//(10**(d//2)))
		#right = i%(10**(d//2))
		#print(left,right,i)
		#if left == right:
		if re.fullmatch(r'(.+)\1', str(i)):
			#print(i)
			s+=i
print('part1', s)
