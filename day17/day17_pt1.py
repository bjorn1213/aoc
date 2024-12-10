from pathlib import Path

dirpath = Path("day17")
fname = dirpath / "day17.txt"
# fname = dirpath / "day17_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
