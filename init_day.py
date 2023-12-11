from pathlib import Path
import shutil
import os

day = 11

dirpath = Path(f"day{day}")
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

os.mkdir(dirpath)
open(dirpath / f"day{day}.txt", "w").close()
open(dirpath / f"day{day}_small.txt", "w").close()
contents = f"""from pathlib import Path

dirpath = Path("day{day}")
fname = dirpath / "day{day}.txt"
# fname = dirpath / "day{day}_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

"""

with open(dirpath / f"day{day}_pt1.py", "w") as f:
    f.write(contents)

with open(dirpath / f"day{day}_pt2.py", "w") as f:
    f.write(contents)
