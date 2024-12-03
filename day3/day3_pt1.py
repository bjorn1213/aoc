from pathlib import Path
import re

dirpath = Path("day3")
fname = dirpath / "day3.txt"
# fname = dirpath / "day3_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

memory = "".join(lines)

m = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

score = 0

for i in m:
    a, b = re.findall(r"\d+", i)
    a = int(a)
    b = int(b)
    score += a * b

print(score)
