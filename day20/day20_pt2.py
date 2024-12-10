from pathlib import Path

dirpath = Path("day20")
fname = dirpath / "day20.txt"
# fname = dirpath / "day20_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
