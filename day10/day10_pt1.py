from pathlib import Path
import re

dirpath = Path("day10")
fname = dirpath / "day10.txt"
# fname = dirpath / "day10_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

width = len(lines[0])
height = len(lines)


def is_valid_location(node):
    return 0 <= node[0] < height and 0 <= node[1] < width


def get_neighbours(node):
    neighbours = set()
    nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in nbs:
        nb = tuple(n1 + d1 for n1, d1 in zip(node, delta))
        if is_valid_location(nb):
            neighbours.add(nb)
    return neighbours


def altitude(node):
    alt = lines[node[0]][node[1]]
    if alt == ".":
        return 10000
    return int(lines[node[0]][node[1]])


def get_score(origin_node):
    origin = origin_node
    visited = set()
    visited.add(origin)
    currently_exploring = set()
    currently_exploring.add(origin)
    score = 0

    while len(currently_exploring) > 0:
        newly_discovered = set()
        for node in currently_exploring:
            for nb in get_neighbours(node):
                if nb in visited:
                    continue
                if altitude(nb) == altitude(node) + 1:
                    newly_discovered.add(nb)
        visited = visited.union(currently_exploring)
        currently_exploring = newly_discovered

    for node in visited:
        if altitude(node) == 9:
            score += 1
    return score


scores = {}
total_score = 0
for row_idx, line in enumerate(lines):
    for col_idx in [i.start() for i in re.finditer("0", line)]:
        origin_node = (row_idx, col_idx)
        score = get_score(origin_node)
        scores[origin_node] = score
        total_score += score

print(total_score)
