
from pathlib import Path

dirpath = Path("day6")
fname = dirpath / "day6.txt"
# fname = dirpath / "day6_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    