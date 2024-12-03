
from pathlib import Path

dirpath = Path("day5")
fname = dirpath / "day5.txt"
# fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    