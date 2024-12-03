from pathlib import Path
import re

dirpath = Path("day3")
fname = dirpath / "day3.txt"
# fname = dirpath / "day3_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

memory = "".join(lines)

m = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", memory)

score = 0
enabled = True

for instruction in m:
    if instruction[0] != "":
        i = instruction[0]
    elif instruction[1] != "":
        i = instruction[1]
    else:
        i = instruction[-1]

    if i == "do()":
        enabled = True
    elif i == "don't()":
        enabled = False
    else:
        if enabled:
            a, b = re.findall(r"\d+", i)
            a = int(a)
            b = int(b)
            score += a * b

print(score)
