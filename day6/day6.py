import re
import numpy as np
import math

with open(r"AoC2023\day6\day6_input.txt") as f:
    # with open(r"AoC2023\day6\day6_inputsmall.txt") as f:
    lines = f.readlines()


l = lines[0].replace("\n", "")
_, times = l.split(":")
times = [int(t) for t in times.split(" ") if t.isnumeric()]

l = lines[1].replace("\n", "")
_, distances = l.split(":")
distances = [int(t) for t in distances.split(" ") if t.isnumeric()]


def get_option_count(t, d):
    sol1 = (1 / 2) * (t - math.sqrt(t**2 - 4 * d)) + 10 ** (-5)
    sol2 = (1 / 2) * (t + math.sqrt(t**2 - 4 * d)) - +(10 ** (-5))

    return min(math.floor(sol2), t) - max(math.ceil(sol1), 0) + 1


total = 1
for t, d in zip(times, distances):
    options = get_option_count(t, d)
    total *= options
    # print(t, d, options)

# pt 1
print(total)

# pt 2
print(get_option_count(38947970, 241154910741091))
