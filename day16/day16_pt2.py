from pathlib import Path

dirpath = Path("day16")
fname = dirpath / "day16.txt"
# fname = dirpath / "day16_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
