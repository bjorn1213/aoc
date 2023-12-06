from pathlib import Path
import numpy as np

dirpath = Path("day5")
# fname = dirpath / "day5.txt"
fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def merge_maps(map1, map2):
    it1 = iter(sorted(map1, key=lambda x: x[0]))
    it2 = iter(sorted(map2, key=lambda x: x[0]))

    def get_next(it):
        try:
            return next(it)
        except:
            return None

    rng1 = get_next(it1)
    rng2 = get_next(it2)

    new_maps = []

    prev_min = -np.inf

    while rng1 or rng2:
        if rng1 is None:
            lb, ub, delta = rng2
            rng2 = get_next(it2)
        elif rng2 is None:
            lb, ub, delta = rng1
            rng1 = get_next(it1)
        else:
            x = np.argmin([rng1[0], rng2[0]])
            y = np.argmin([rng1[1], rng2[1]])

            z = [rng1, rng2]
            lb = np.maximum(z[x][0], prev_min)
            ub = z[y][1]
            delta = rng1[2] + rng2[2]

            prev_min = lb + 1

            if y == 0:
                rng2 = (ub + 1, rng2[1], rng2[2])
                rng1 = get_next(it1)
            else:
                rng1 = (ub + 1, rng1[1], rng1[2])
                rng2 = get_next(it2)
        n = (lb, ub, delta)
        new_maps.append(n)

    return new_maps


total_map = [(0, np.inf, 0)]
cur_map = []
prevline = ""
for line in lines:
    l = line.replace("\n", "")

    if "seeds:" in l:
        _, l = l.split(":")
        seeds = set([int(s) for s in l.split(" ") if s != ""])
    elif l == "":
        continue
    elif not l[0].isnumeric():
        print()
        print(prevline)
        prevline = l
        total_map = merge_maps(total_map, cur_map)
        cur_map = []
        for m in sorted(total_map, key=lambda x: x[0]):
            print(m)
    else:
        dst_start, src_start, length = [int(x) for x in l.split(" ")]
        cur_map.append((src_start, src_start + length - 1, dst_start - src_start))


print(seeds)
