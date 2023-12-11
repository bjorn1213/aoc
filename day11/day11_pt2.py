from pathlib import Path

dirpath = Path("day11")
fname = dirpath / "day11.txt"
# fname = dirpath / "day11_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

