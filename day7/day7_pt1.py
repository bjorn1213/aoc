
from pathlib import Path

dirpath = Path("day7")
fname = dirpath / "day7.txt"
# fname = dirpath / "day7_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

    