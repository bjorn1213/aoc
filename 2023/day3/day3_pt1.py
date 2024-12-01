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

part_coords = set()
symbol_coords = set()

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

print(matrix)

total = 0

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
        else:
            print(m.group(0))

print(total)

# class PotentialPart():
#     coordinates = set()
#     isPartnumber = False

#     def add_coordinate(self, coordinate, isPart):
#         self.coordinates.add(coordinate)
#         self.isPartnumber = bool(self.isPartnumber + isPart)

# potentialParts = []
# coord_parts = {}

# def check_coordinate(c):
#     cx, cy = c
#     isPartnumber = False
#     connectedParts = []
#     for x in range(cx-1, cx+2):
#         for y in range(cy-1, cy+2):
#             if x == y == 0:
#                 continue
#             if (x, y) in symbol_coords:
#                 isPartnumber = True
#             if (x, y) in coord_parts:
#                 connectedParts.append(coord_parts[(x, y)])
#     if len(connectedParts) == 0:
#         pot_part = PotentialPart()
#         pot_part.add_coordinate(c, isPartnumber)
#         coord_parts[c] = pot_part
#     else:
#         for part in connectedParts:
#             part.add_coordinate(c, isPartnumber)
#             coord_parts[part.coordinates].append(c)

# for c in part_coords:
#     check_coordinate(c)
