from pathlib import Path
import numpy as np

dirpath = Path("day10")
fname = dirpath / "day10.txt"
# fname = dirpath / "day10_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

s_coord = [0, 0]

grid = np.full((len(lines), len(lines[0]) - 1), ".", dtype=str)

for i, line in enumerate(lines):
    l = line.replace("\n", "")

    for j, node in enumerate(l):
        grid[i, j] = node
        if node == "S":
            s_coord = np.array([i, j])

d = {
    "|": [np.array([1, 0]), np.array([-1, 0])],
    "-": [np.array([0, 1]), np.array([0, -1])],
    "L": [np.array([-1, 0]), np.array([0, 1])],
    "J": [np.array([-1, 0]), np.array([0, -1])],
    "7": [np.array([0, -1]), np.array([1, 0])],
    "F": [np.array([0, 1]), np.array([1, 0])],
}


def x(node, position):
    deltas = d[node]

    return [d + position for d in deltas]


node = "S"
coord = np.array(s_coord)
coords = [coord]
steps = [0]

prev_coord = np.array(coord)
coord = coord + np.array([0, 1])
node = grid[*coord]
coords.append(coord)
steps.append(max(steps) + 1)

while node != "S":
    candidates = x(node, coord)
    next_coord = (
        candidates[0] if all(np.equal(candidates[1], prev_coord)) else candidates[1]
    )
    prev_coord = coord
    coord = next_coord
    node = grid[*coord]
    coords.append(coord)
    steps.append(max(steps) + 1)


distances = [min(s1, s2) for s1, s2 in zip(steps, steps[::-1])]
print(max(distances))
