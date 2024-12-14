from pathlib import Path
import re
import numpy as np

dirpath = Path("day13")
fname = dirpath / "day13.txt"
# fname = dirpath / "day13_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]


cost = np.array([3, 1])
total_cost = 0
for line in lines:
    if "Button A" in line:
        numbers = (int(i) for i in re.findall(r"\d+", line))
        a_x, a_y = numbers
    elif "Button B" in line:
        numbers = (int(i) for i in re.findall(r"\d+", line))
        b_x, b_y = numbers
    elif "Prize" in line:
        numbers = (int(i) for i in re.findall(r"\d+", line))
        target_x, target_y = numbers
        coeff = np.array([[a_x, b_x], [a_y, b_y]])

        target = np.array([target_x, target_y])

        x = np.linalg.solve(coeff, target).T
        if all(round(i, 0) == round(i, 3) for i in x):
            cur_cost = x[0] * cost[0] + x[1] * cost[1]

            total_cost += cur_cost

print(total_cost)
