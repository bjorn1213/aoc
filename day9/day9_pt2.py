
from pathlib import Path

dirpath = Path("day9")
fname = dirpath / "day9.txt"
# fname = dirpath / "day9_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    