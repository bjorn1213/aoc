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


def sploosh(area_id, node, direction, visited):
    visited.add(node)

    if direction == "d":
        # go left
        cur_node = node
        while True:
            next_node = (cur_node[0], cur_node[1] - 1)
            diag_node = (cur_node[0] + 1, cur_node[1] - 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node

        # go right
        cur_node = node
        while True:
            next_node = (cur_node[0], cur_node[1] + 1)
            diag_node = (cur_node[0] + 1, cur_node[1] + 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node
    elif direction == "u":
        # go left
        cur_node = node
        while True:
            next_node = (cur_node[0], cur_node[1] - 1)
            diag_node = (cur_node[0] - 1, cur_node[1] - 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node

        # go right
        cur_node = node
        while True:
            next_node = (cur_node[0], cur_node[1] + 1)
            diag_node = (cur_node[0] - 1, cur_node[1] + 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node
    elif direction == "r":
        # go up
        cur_node = node
        while True:
            next_node = (cur_node[0] - 1, cur_node[1])
            diag_node = (cur_node[0] - 1, cur_node[1] + 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node

        # go down
        cur_node = node
        while True:
            next_node = (cur_node[0] + 1, cur_node[1])
            diag_node = (cur_node[0] + 1, cur_node[1] + 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node
    elif direction == "l":
        # go up
        cur_node = node
        while True:
            next_node = (cur_node[0] - 1, cur_node[1])
            diag_node = (cur_node[0] - 1, cur_node[1] - 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node

        # go down
        cur_node = node
        while True:
            next_node = (cur_node[0] + 1, cur_node[1])
            diag_node = (cur_node[0] + 1, cur_node[1] - 1)
            if next_node in area_node_mapping[area_id]:
                break
            if diag_node not in area_node_mapping[area_id]:
                break
            visited.add(next_node)
            cur_node = next_node


total_cost = 0
for area_id in area_node_mapping:
    nodes = area_node_mapping[area_id]

    max_row_idx = 0
    min_row_idx = height - 1
    max_col_idx = 0
    min_col_idx = width - 1

    for node in nodes:
        min_row_idx = min(node[0], min_row_idx)
        min_col_idx = min(node[1], min_col_idx)
        max_row_idx = max(node[0], max_row_idx)
        max_col_idx = max(node[1], max_col_idx)

    side_count = 0

    for direction in "urdl":
        visited_nodes = set()

        if direction == "d":
            for col_idx in range(min_col_idx, max_col_idx + 1):
                row_idx = min_row_idx - 1
                prev_node = (row_idx, col_idx)

                for row_idx in range(min_row_idx, max_row_idx + 1):
                    node = (row_idx, col_idx)
                    if prev_node not in nodes and node in nodes:
                        if prev_node not in visited_nodes:
                            side_count += 1
                            sploosh(
                                area_id=area_id,
                                node=prev_node,
                                direction=direction,
                                visited=visited_nodes,
                            )
                    prev_node = node
        elif direction == "u":
            for col_idx in range(min_col_idx, max_col_idx + 1):
                row_idx = max_row_idx + 1
                prev_node = (row_idx, col_idx)

                for row_idx in reversed(range(min_row_idx, max_row_idx + 1)):
                    node = (row_idx, col_idx)
                    if prev_node not in nodes and node in nodes:
                        if prev_node not in visited_nodes:
                            side_count += 1
                            sploosh(
                                area_id=area_id,
                                node=prev_node,
                                direction=direction,
                                visited=visited_nodes,
                            )
                    prev_node = node
        elif direction == "r":
            for row_idx in range(min_row_idx, max_row_idx + 1):
                col_idx = min_col_idx - 1
                prev_node = (row_idx, col_idx)

                for col_idx in range(min_col_idx, max_col_idx + 1):
                    node = (row_idx, col_idx)
                    if prev_node not in nodes and node in nodes:
                        if prev_node not in visited_nodes:
                            side_count += 1
                            sploosh(
                                area_id=area_id,
                                node=prev_node,
                                direction=direction,
                                visited=visited_nodes,
                            )
                    prev_node = node
        elif direction == "l":
            for row_idx in range(min_row_idx, max_row_idx + 1):
                col_idx = max_col_idx + 1
                prev_node = (row_idx, col_idx)

                for col_idx in reversed(range(min_col_idx, max_col_idx + 1)):
                    node = (row_idx, col_idx)
                    if prev_node not in nodes and node in nodes:
                        if prev_node not in visited_nodes:
                            side_count += 1
                            sploosh(
                                area_id=area_id,
                                node=prev_node,
                                direction=direction,
                                visited=visited_nodes,
                            )
                    prev_node = node

    area = len(area_node_mapping[area_id])
    cost = area * side_count
    total_cost += cost

print(total_cost)
