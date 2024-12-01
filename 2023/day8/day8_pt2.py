from pathlib import Path
from itertools import cycle
import re

dirpath = Path("day8")
fname = dirpath / "day8.txt"
# fname = dirpath / "day8_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return self.name

    def __getitem__(self, item):
        if item == "L":
            return self.left
        return self.right


nodes = {}

for idx, line in enumerate(lines):
    l = line.replace("\n", "")
    if idx == 0:
        navigator = cycle(l)
    elif idx == 1:
        continue
    else:
        node_name, children = l.split("=")
        node_name = node_name.replace(" ", "")
        children = re.sub(r"[\(\)\s]", "", children)
        left_name, right_name = children.split(",")
        nodes[node_name] = Node(node_name, left_name, right_name)


cur_nodes = [node for node in nodes.keys() if node[-1] == "A"]
counters = [0 for _ in cur_nodes]
hits = [[] for _ in cur_nodes]

counter = 0
while not all(node[-1] == "Z" for node in cur_nodes):
    counter += 1
    navigation = next(navigator)
    next_nodes = [nodes[cur_node][navigation] for cur_node in cur_nodes]
    cur_nodes = next_nodes

    if any(node[-1] == "Z" for node in cur_nodes):
        print("\n" * 4)
        for i, n in enumerate(cur_nodes):
            if n[-1] == "Z":
                hits[i].append(counter / 281)
            print(hits[i])
        print()
print(counter)
