from pathlib import Path
import numpy as np

np.set_printoptions(linewidth=200, formatter={"numpystr": lambda x: x})


dirpath = Path("day11")
fname = dirpath / "day11.txt"
fname = dirpath / "day11_small.txt"

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

x_vals = list(h_duplicates) + list(range(len(lines[0]) - 1))
x_vals.sort()

y_vals = list(v_duplicates) + list(range(len(lines)))
y_vals.sort()

grid = np.vstack(tuple(grid[i, :] for i in y_vals))
grid = np.vstack(tuple(grid[:, i] for i in x_vals)).T

coords = [(i, j) for i, j in zip(*np.where(grid == "#"))]

total = 0
for c1 in coords:
    for c2 in coords:
        dist = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
        total += dist
print(total / 2)
