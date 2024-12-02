from pathlib import Path
import re

dirpath = Path("day1")
fname = dirpath / "day1.txt"
# fname = dirpath / "day1_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

numbers1 = []
numbers2 = []

for line in lines:
    m = re.match(r"(\d+)\s+(\d+)", line)
    numbers1.append(int(m[1]))
    numbers2.append(int(m[2]))

numbers1.sort()
numbers2.sort()

total_diff = 0

for n1, n2 in zip(numbers1, numbers2):
    total_diff += abs(n1 - n2)

print(total_diff)
