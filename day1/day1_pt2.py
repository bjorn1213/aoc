from pathlib import Path
import re

dirpath = Path("day1")
fname = dirpath / "day1.txt"
# fname = dirpath / "day1_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

numbers1 = []
n2_freq = {}

for line in lines:
    m = re.match(r"(\d+)\s+(\d+)", line)
    numbers1.append(int(m[1]))
    n2 = int(m[2])
    n2_freq[n2] = n2_freq.get(n2, 0) + 1

score = 0

for n in numbers1:
    score += n * n2_freq.get(n, 0)

print(score)
