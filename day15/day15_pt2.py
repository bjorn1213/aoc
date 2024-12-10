from pathlib import Path

dirpath = Path("day15")
fname = dirpath / "day15.txt"
# fname = dirpath / "day15_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
