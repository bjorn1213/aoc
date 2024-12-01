from pathlib import Path

dirpath = Path("day4")
fname = dirpath / "day4.txt"
# fname = dirpath / "day4_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.replace("\n", "")
    _, sets = line.split(":")

    winning, gotten = sets.split("|")
    winning = [int(n) for n in winning.split(" ") if n != ""]
    gotten = [int(n) for n in gotten.split(" ") if n != ""]

    winning = set(winning)
    gotten = set(gotten)

    intersect = set.intersection(winning, gotten)
    if len(intersect) > 0:
        total += 2 ** (len(intersect) - 1)

print(total)
