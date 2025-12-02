#!/usr/bin/env python3
from argparse import ArgumentParser
from requests import get
import os

parser = ArgumentParser()
parser.add_argument("day", type=int)
args = parser.parse_args()


os.makedirs(f"day{args.day}", exist_ok=True)
if os.path.exists("session.txt"):
	with open("session.txt") as f:
        	session = f.read().strip()
	with open(f"day{args.day}/input.txt", "w") as f:
		f.write(get(f"https://adventofcode.com/2025/day/{args.day}/input", cookies={"session": session}).text)

if not os.path.exists(f"day{args.day}/part1.py"):
  with open(f"day{args.day}/part1.py", "w") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write("\nprint('part1')\n")
  os.chmod(f"day{args.day}/part1.py", 0o755)
if not os.path.exists(f"day{args.day}/part2.py"):
  with open(f"day{args.day}/part2.py", "w") as f:
    f.write("#!/usr/bin/env python3\n")
    f.write("\nprint('part2')\n")
  os.chmod(f"day{args.day}/part2.py", 0o755)
