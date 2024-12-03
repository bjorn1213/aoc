from pathlib import Path
import numpy as np
import re

dirpath = Path("day2")
fname = dirpath / "day2.txt"
# fname = dirpath / "day2_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def check_levels(levels, can_dampen=True):
    diff_arr = levels[1:] - levels[:-1]

    is_safe = False

    if all(diff_arr < 0):
        is_safe = not any((diff_arr < -3) | (diff_arr > -1))
    elif all(diff_arr > 0):
        is_safe = not any((diff_arr < 1) | (diff_arr > 3))
    else:
        is_safe = False

    if not is_safe and can_dampen:
        for i in range(len(levels)):
            updated_levels = np.delete(levels, i)
            is_safe = is_safe or check_levels(updated_levels, can_dampen=False)
            if is_safe:
                break
    return is_safe


score = 0

for i, line in enumerate(lines):
    m = re.finditer(r"(\d+)", line)
    levels = np.array([int(i.group(0)) for i in m])

    if check_levels(levels):
        score += 1

print(score)
