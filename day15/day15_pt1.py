from pathlib import Path
from typing import Literal

dirpath = Path("day15")
fname = dirpath / "day15.txt"
# fname = dirpath / "day15_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

height = len(lines) - 2
width = len(lines[0])

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]
NodeType = Literal["Box", "Robot", "Wall", "Empty"]
node_type_mapping: dict[str, NodeType] = {
    "@": "Robot",
    "#": "Wall",
    ".": "Empty",
    "O": "Box",
}
node_type_mapping_inv = {v: k for k, v in node_type_mapping.items()}
movement_mapping: dict[str, Direction] = {
    "^": UP,
    "v": DOWN,
    "<": LEFT,
    ">": RIGHT,
}

coordinate_node_map = {}


class Node:
    def __init__(self, coordinates: tuple[int, int], node_type: NodeType):
        self.coordinates = coordinates
        self.node_type: NodeType = node_type

    def get_GPS(self) -> int:
        return self.coordinates[0] + self.coordinates[1] * 100

    def get_neighbour(self, direction: Direction):
        delta = {
            UP: (0, -1),
            DOWN: (0, 1),
            LEFT: (-1, 0),
            RIGHT: (1, 0),
        }
        change = delta[direction]
        new_coordinate = (
            self.coordinates[0] + change[0],
            self.coordinates[1] + change[1],
        )

        if new_coordinate in coordinate_node_map:
            return coordinate_node_map[new_coordinate]
        return None

    def move(self, direction: Direction, new_type: NodeType):
        nb: Node = self.get_neighbour(direction=direction)
        if not nb:
            # shouldn't happen
            return False
        elif self.node_type == "Wall":
            return False
        elif self.node_type == "Empty" or nb.move(
            direction=direction, new_type=self.node_type
        ):
            self.node_type = new_type
            return True
        else:
            return False


coordinate_node_map: dict[tuple[int, int], Node] = {}

robot_location = None


for y, line in enumerate(lines):
    if ">" in line:
        # handle this later
        continue
    elif line == "":
        continue
    else:
        for x, character in enumerate(line):
            coordinates = (x, y)
            node_type = node_type_mapping[character]
            coordinate_node_map[coordinates] = Node(
                coordinates=coordinates, node_type=node_type
            )
            if node_type == "Robot":
                robot_location = coordinates


def print_grid():
    for y in range(height):
        for x in range(width):
            coordinates = (x, y)
            node: Node = coordinate_node_map[coordinates]
            print(node_type_mapping_inv[node.node_type], end="")
        print()


# print_grid()

robot_node: Node = coordinate_node_map[robot_location]
for character in lines[-1]:
    direction = movement_mapping[character]
    if robot_node.move(direction=direction, new_type="Empty"):
        robot_node = robot_node.get_neighbour(direction)

    # print(f"\nMoved {character}\n")
    # print_grid()

total = 0
for location, node in coordinate_node_map.items():
    if node.node_type == "Box":
        total += node.get_GPS()
print(total)
