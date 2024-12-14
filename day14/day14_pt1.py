from pathlib import Path
import re

dirpath = Path("day14")
fname = dirpath / "day14.txt"
fname = dirpath / "day14_small.txt"

if fname == dirpath / "day14.txt":
    width = 101
    height = 103
else:
    width = 11
    height = 7

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

SECONDS = 100
robot_count = {}

for line in lines:
    numbers = re.findall(r"[-]*\d+", line)
    px, py, vx, vy = (int(i) for i in numbers)

    new_x = (px + SECONDS * vx) % width
    new_y = (py + SECONDS * vy) % height
    new_pos = (new_x, new_y)

    robot_count[new_pos] = robot_count.get(new_pos, 0) + 1

LT = "LT"
RT = "RT"
LB = "LB"
RB = "RB"

quadrant_count = {q: 0 for q in [LT, RT, RB, LB]}

for position, rcount in robot_count.items():
    if position[0] < width // 2:
        if position[1] < height // 2:
            quadrant_count[LT] += rcount
        elif position[1] > height // 2:
            quadrant_count[RT] += rcount
    elif position[0] > width // 2:
        if position[1] < height // 2:
            quadrant_count[LB] += rcount
        elif position[1] > height // 2:
            quadrant_count[RB] += rcount

score = 1
for val in quadrant_count.values():
    score *= val

for k, v in sorted(quadrant_count.items()):
    print(k, v)

for y in range(height):
    for x in range(width):
        print(robot_count.get((x, y), "."), end="")
    print()

print(score)
