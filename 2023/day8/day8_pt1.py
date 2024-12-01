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


cur_node = "AAA"
counter = 0
while cur_node != "ZZZ":
    counter += 1
    navigation = next(navigator)
    next_node = nodes[cur_node][navigation]
    cur_node = next_node
print(counter)
