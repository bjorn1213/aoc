from pathlib import Path
import re
from itertools import combinations

dirpath = Path("day8")
fname = dirpath / "day8.txt"
# fname = dirpath / "day8_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

width = len(lines[0])
height = len(lines)

locations = {}

for row_idx, line in enumerate(lines):
    m = [i for i in re.finditer(r"[^\.]", line)]
    if len(m) == 0:
        continue

    for antenna_match in m:
        col_idx = antenna_match.start()
        coordinates = (row_idx, col_idx)
        antenna = antenna_match[0]
        cur_locations = locations.get(antenna, [])
        cur_locations.append(coordinates)
        locations[antenna] = cur_locations

antinodes = set()


def check_antinode(antinode):
    if (0 <= antinode[0] < height) and (0 <= antinode[1] < width):
        return True
    return False


for antenna in locations:
    for loc1, loc2 in combinations(locations[antenna], 2):
        row_delta = loc1[0] - loc2[0]
        col_delta = loc1[1] - loc2[1]

        antinode = loc1
        while check_antinode(antinode):
            antinodes.add(antinode)

            antinode_row_idx = antinode[0] + row_delta
            antinode_col_idx = antinode[1] + col_delta
            antinode = (antinode_row_idx, antinode_col_idx)

        antinode = loc1
        while check_antinode(antinode):
            antinodes.add(antinode)

            antinode_row_idx = antinode[0] - row_delta
            antinode_col_idx = antinode[1] - col_delta
            antinode = (antinode_row_idx, antinode_col_idx)


print(len(antinodes))
