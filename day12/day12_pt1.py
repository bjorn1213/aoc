from pathlib import Path

dirpath = Path("day12")
fname = dirpath / "day12.txt"
# fname = dirpath / "day12_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

width = len(lines[0])
height = len(lines)


def get_symbol(node):
    sym = lines[node[0]][node[1]]
    return sym


def is_valid_location(node):
    return 0 <= node[0] < height and 0 <= node[1] < width


def get_neighbours(node, ignore_oos=True):
    neighbours = set()
    nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in nbs:
        nb = tuple(n1 + d1 for n1, d1 in zip(node, delta))
        if is_valid_location(nb) or not ignore_oos:
            neighbours.add(nb)
    return neighbours


node_area_mapping = {}
last_area_id = 0


def explore_area(node):
    node_area_mapping[node] = last_area_id
    cur_sym = get_symbol(node)
    nbs = get_neighbours(node)
    for nb in nbs:
        if nb in node_area_mapping:
            continue
        if get_symbol(nb) == cur_sym:
            explore_area(nb)


for row_idx in range(height):
    for col_idx in range(width):
        node = (row_idx, col_idx)
        if node in node_area_mapping:
            continue
        explore_area(node)
        last_area_id += 1

area_node_mapping = {}

for node, area_id in node_area_mapping.items():
    node_set = set()
    node_set.add(node)
    s = area_node_mapping.get(area_id, set())
    area_node_mapping[area_id] = s.union(node_set)

area_perimeter = {}
for area, node_set in area_node_mapping.items():
    total_perimeter = 0
    for node in node_set:
        nbs = get_neighbours(node, ignore_oos=False)
        for nb in nbs:
            if nb not in node_set:
                total_perimeter += 1
    area_perimeter[area] = total_perimeter

total_price = 0

for area in area_node_mapping:
    total_price += area_perimeter[area] * len(area_node_mapping[area])
print(total_price)
