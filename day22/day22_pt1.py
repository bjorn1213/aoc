from pathlib import Path

dirpath = Path("day22")
fname = dirpath / "day22.txt"
# fname = dirpath / "day22_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
