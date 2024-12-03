
from pathlib import Path

dirpath = Path("day4")
fname = dirpath / "day4.txt"
# fname = dirpath / "day4_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    