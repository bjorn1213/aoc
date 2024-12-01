from pathlib import Path
import numpy as np

np.set_printoptions(linewidth=200, formatter={"numpystr": lambda x: x})


dirpath = Path("day11")
fname = dirpath / "day11.txt"
# fname = dirpath / "day11_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

grid = np.full((len(lines), len(lines[0]) - 1), "", dtype=str)

for i, line in enumerate(lines):
    l = line.replace("\n", "")
    grid[i, :] = list(l)
print(grid)

x = 1

h_duplicates = np.where(np.all(grid == ".", axis=0))[0]
v_duplicates = np.where(np.all(grid == ".", axis=1))[0]

coords = [(i, j) for i, j in zip(*np.where(grid == "#"))]

dup_factor = 1_000_000

total = 0
for c1 in coords:
    for c2 in coords:
        h_dups = (
            (min(c1[0], c2[0]) <= v_duplicates) & (v_duplicates <= max(c1[0], c2[0]))
        ).sum()
        v_dups = (
            (min(c1[1], c2[1]) <= h_duplicates) & (h_duplicates <= max(c1[1], c2[1]))
        ).sum()
        dist = (
            abs(c1[0] - c2[0])
            + abs(c1[1] - c2[1])
            + (max(0, h_dups) + max(0, v_dups)) * dup_factor
            - v_dups
            - h_dups
        )
        total += dist
print(total / 2)
