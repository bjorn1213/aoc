
from pathlib import Path

dirpath = Path("day8")
fname = dirpath / "day8.txt"
# fname = dirpath / "day8_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    