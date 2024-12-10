from pathlib import Path
import re
from itertools import cycle

dirpath = Path("day6")
fname = dirpath / "day6.txt"
# fname = dirpath / "day6_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]

width = len(lines[0])
height = len(lines)

blocks = set()

for row_idx, row in enumerate(lines):
    for col_idx in [s.start() for s in re.finditer(r"#", row)]:
        blocks.add((row_idx, col_idx))

    for start_col_idx in [s.start() for s in re.finditer(r"\^", row)]:
        start_pos = (row_idx, start_col_idx)

UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"
LEFT = "LEFT"


def add_tuples(t1, t2):
    return tuple((x + y for x, y in zip(t1, t2)))


direction_delta = {
    UP: (-1, 0),
    RIGHT: (0, 1),
    LEFT: (0, -1),
    DOWN: (1, 0),
}

possible_obstacle_positions = set()


def valid_position(position):
    row_idx, col_idx = position
    if row_idx < 0 or col_idx < 0 or row_idx >= height or col_idx >= width:
        return False
    return True


total_options = width * height


for row_idx in range(height):
    for col_idx in range(width):
        tried_options = row_idx * width + col_idx
        print(f"{tried_options}/{total_options} ({tried_options/total_options})")
        obstacle_pos = (row_idx, col_idx)
        if obstacle_pos in blocks or obstacle_pos == start_pos:
            continue

        position = start_pos
        cur_dir = UP
        visited = set()
        direction_cycle = cycle((RIGHT, DOWN, LEFT, UP))

        while valid_position(position) and (*position, cur_dir) not in visited:
            visited.add((*position, cur_dir))
            new_pos = add_tuples(position, direction_delta[cur_dir])
            if new_pos in blocks or new_pos == obstacle_pos:
                cur_dir = next(direction_cycle)
                continue
            else:
                position = new_pos
        if (*position, cur_dir) in visited:
            possible_obstacle_positions.add(obstacle_pos)


print(len(possible_obstacle_positions))
