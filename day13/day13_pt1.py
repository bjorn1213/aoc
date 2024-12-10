from pathlib import Path

dirpath = Path("day13")
fname = dirpath / "day13.txt"
# fname = dirpath / "day13_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
