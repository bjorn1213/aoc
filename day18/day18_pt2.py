from pathlib import Path

dirpath = Path("day18")
fname = dirpath / "day18.txt"
# fname = dirpath / "day18_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
