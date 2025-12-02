#!/usr/bin/env python3
import math
import re

def alleq(it):
	first = next(it)
	return all(x == first for x in it)

def chunkstring(string, length):
    return {string[0+i:length+i] for i in range(0, len(string), length)}

def ci(i):
	ni = int(math.log10(i))+1
	#print(i,ni)
	for d in range(1, ni//2+1):
		#print(i,ni,{cib(i,d,n) for n in range(ni//d)})
		if ni%d==0 and ideal(i,d,ni):
			return True
	return False


def ideal(i,d,ni):
	r = 0
	p = i % 10**d
	for n in range(ni//d):
		r += p*(10**(d*n))
		if r > i:
			return False
		#print(r,i,p)
	return r == i
def cib(i,d,n):
	return (i // (10**(d*n))) % (10**d)

#print([cib(22,1,n) for n in range(int(math.log10(22))+1)])

with open("input.txt", "r") as f:
	ranges = [(int((p:=r.split("-"))[0]),int(p[1])) for r in f.read().strip().split(",")]
s=0
for r in ranges:
	skip = False
	for i in range(r[0],r[1]+1):
		if re.fullmatch(r'(.+)\1+', str(i)):
			s+=i
			skip = True
			#print(i)
print('part2', s)
