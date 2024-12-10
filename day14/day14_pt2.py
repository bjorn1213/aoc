from pathlib import Path

dirpath = Path("day14")
fname = dirpath / "day14.txt"
# fname = dirpath / "day14_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
