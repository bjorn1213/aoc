import numpy as np

map1 = [(0, np.inf, 0)]

map2 = [(98, 99, -48), (50, 97, 2)]

map3 = [
    (0, 14, 39),
    (15, 51, -15),
    (52, 53, -15),
]
# map2 = [(10, 20, 1)]


def add_map_to_maplist(maplist, map):
    new_maplist = []

    for curmap in sorted(maplist, key=lambda x: x[0]):
        # curmap is left(overlapping) of map
        if curmap[0] <= map[0] <= curmap[1] <= map[1]:
            new_maplist.append((map[0], curmap[1], curmap[2] + map[2]))
            if curmap[0] < map[0]:
                new_maplist.append((curmap[0], map[0] - 1, curmap[2]))

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


def get_new_ranges(maplist, map):
    delta = map[2]
    new_ranges = []

    maplist = sorted(maplist, key=lambda x: x[0])
    maparray = np.array(maplist)

    while map:
        if np.where(maparray[:, 1] > map[0])[0].size > 0:
            idx = np.where(maparray[:, 1] > map[0])[0][0]

            new_ranges.append((map[0], maparray[idx, 1], maparray[idx, 2] + map[2]))
            if map[1] > maparray[idx, 1]:
                map = (maparray[idx, 1] + 1, map[1], map[2])
            else:
                break
        else:
            new_ranges.append(map)
            break
    return [(r[0] - delta, r[1] - delta, r[2]) for r in new_ranges]


def merge_maps(map1, map2):
    merged_maps = []

    for map in map1:
        map_adjusted = (map[0] + map[2], map[1] + map[2], map[2])
        new_ranges = get_new_ranges(map2, map_adjusted)
        merged_maps += new_ranges

    return merged_maps


x = merge_maps(map1, map2)

for m in x:
    print(m)
