from pathlib import Path
import re
import time
import numpy as np
from PIL import Image

dirpath = Path("day14")
fname = dirpath / "day14.txt"
# fname = dirpath / "day14_small.txt"

if fname == dirpath / "day14.txt":
    width = 101
    height = 103
else:
    width = 11
    height = 7

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

SECOND_DELTA = 5000
START_SECONDS = 0
SECONDS = 5000
go = True

while go:
    for second in range(START_SECONDS, SECONDS):
        robot_count = {}
        for line in lines:
            numbers = re.findall(r"[-]*\d+", line)
            px, py, vx, vy = (int(i) for i in numbers)

            new_x = (px + second * vx) % width
            new_y = (py + second * vy) % height
            new_pos = (new_x, new_y)

            robot_count[new_pos] = robot_count.get(new_pos, 0) + 1

        img_data = np.zeros((width, height, 3), dtype=np.uint8)
        comp_data = np.zeros((width, height, 1), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                robots = robot_count.get((x, y), 0)
                if robots > 0:
                    img_data[x, y] = [255, 255, 255]
                    comp_data[x, y] = 1
        save_img = False
        for x in range(width):
            col = comp_data[x, :]
            unique, counts = np.unique(col, return_counts=True)
            counter = dict(zip([int(i) for i in unique], [int(i) for i in counts]))
            if counter.get(1, 0) > 25:
                save_img = True
                break
        if save_img:
            Image.fromarray(img_data).save(dirpath / "images" / f"{second}.png")
    START_SECONDS = SECONDS
    SECONDS += 5000
    fb = input("continue?")
    if fb != "":
        break

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

print(score)
