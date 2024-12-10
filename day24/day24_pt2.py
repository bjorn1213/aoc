from pathlib import Path

dirpath = Path("day24")
fname = dirpath / "day24.txt"
# fname = dirpath / "day24_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
