from pathlib import Path

dirpath = Path("day23")
fname = dirpath / "day23.txt"
# fname = dirpath / "day23_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]
