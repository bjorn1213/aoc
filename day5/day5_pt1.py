from pathlib import Path
import numpy as np

dirpath = Path("day5")
# fname = dirpath / "day5.txt"
fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def add_map_to_maplist(maplist, map):
    new_maplist = []

    for curmap in sorted(maplist, key=lambda x: x[0]):
        # curmap is left(overlapping) of map
        if curmap[0] <= map[0] <= curmap[1] <= map[1]:
            if curmap[0] < map[0]:
                new_maplist.append((curmap[0], map[0] - 1, curmap[2]))
            new_maplist.append((map[0], curmap[1], curmap[2] + map[2]))

        # curmap is right(overlapping) of map
        elif map[0] <= curmap[0] <= map[1] <= curmap[1]:
            new_maplist.append((curmap[0], map[1], map[2] + curmap[2]))
            if map[1] < curmap[1]:
                new_maplist.append((map[1] + 1, curmap[1], curmap[2]))

        # map is contained in curmap
        elif curmap[0] < map[0] <= map[1] < curmap[1]:
            new_maplist.append((curmap[0], map[0] - 1, curmap[2]))
            new_maplist.append((map[0], map[1], curmap[2] + map[2]))
            new_maplist.append((map[1] + 1, curmap[1], curmap[2]))
        # curmap is contained in map
        elif map[0] < curmap[0] <= curmap[1] < map[1]:
            new_maplist.append((curmap[0], curmap[1], curmap[2] + map[2]))
        elif curmap[1] < map[0]:
            new_maplist.append(curmap)
        elif map[1] < curmap[0]:
            new_maplist.append(curmap)
        else:
            print("uncaught!")
    return new_maplist


def merge_maps(map1, map2):
    new_maps = map1
    for map in map2:
        new_maps = add_map_to_maplist(new_maps, map)
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
