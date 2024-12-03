
from pathlib import Path

dirpath = Path("day12")
fname = dirpath / "day12.txt"
# fname = dirpath / "day12_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    