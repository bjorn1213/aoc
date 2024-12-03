
from pathlib import Path

dirpath = Path("day10")
fname = dirpath / "day10.txt"
# fname = dirpath / "day10_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    