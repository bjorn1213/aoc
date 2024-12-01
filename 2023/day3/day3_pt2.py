import math
from pathlib import Path
import numpy as np
import re

dirpath = Path("day3")
fname = dirpath / "day3.txt"
# fname = dirpath / "day3_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

width = len(lines[0]) + 1
height = len(lines) + 1

matrix = np.full((width, height), np.nan)
gear_matrix = np.full((width, height), np.nan, dtype=object)

part_coords = set()
symbol_coords = set()


class Part:
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return str(self.value)
        # return "1.0"

    def __repr__(self):
        return str(self.value)


for line_idx, line in enumerate(lines):
    l = line.replace("\n", "")
    for col_idx, symbol in enumerate(l):
        x = line_idx + 1
        y = col_idx + 1

        if symbol == ".":
            continue
        if symbol.isnumeric():
            matrix[x, y] = int(symbol)
            part_coords.add((x, y))
        else:
            matrix[x, y] = -1.0
            symbol_coords.add((x, y))

# print(matrix)

total = 0

part_coords = {}

for line_idx, line in enumerate(lines):
    x = line_idx + 1
    l = line.replace("\n", "")

    x_min = line_idx
    x_max = line_idx + 3

    for m in re.finditer(r"\d+", l):
        y_min = m.start()
        y_max = m.end() + 2
        if np.any(matrix[x_min:x_max, y_min:y_max] == -1.0):
            total += int(m.group(0))
            # this is a part
            p = Part(int(m.group(0)))
            gear_matrix[line_idx + 1, y_min + 1 : y_max - 1] = p
            part_coords = part_coords | {
                (line_idx + 1, col): int(m.group(0)) for col in range(y_min + 1, y_max)
            }
        else:
            pass

# print(total)

print(gear_matrix)

total = 0

for line_idx, line in enumerate(lines):
    x = line_idx + 1
    l = line.replace("\n", "")

    x_min = line_idx
    x_max = line_idx + 2

    for m in re.finditer(r"\*", l):
        y_min = m.start()
        y_max = m.end() + 1

        parts = set()

        for a in range(x_min, x_max + 1):
            for b in range(y_min, y_max + 1):
                if isinstance(gear_matrix[a, b], Part):
                    parts.add(gear_matrix[a, b])
        if len(parts) == 2:
            total += math.prod([p.value for p in parts])
            pass

print(total)
