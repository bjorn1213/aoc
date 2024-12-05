from pathlib import Path

dirpath = Path("day4")
fname = dirpath / "day4.txt"
# fname = dirpath / "day4_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]

next_letter = {"X": "M", "M": "A", "A": "S", "S": None}

directions = [
    "north",
    "northeast",
    "east",
    "southeast",
    "south",
    "southwest",
    "west",
    "northwest",
]


def get_next_idx(direction, col_idx_ni, row_idx_ni):
    if direction == "north":
        col_idx_new = col_idx_ni
        row_idx_new = row_idx_ni - 1
    elif direction == "northeast":
        col_idx_new = col_idx_ni + 1
        row_idx_new = row_idx_ni - 1
    elif direction == "east":
        col_idx_new = col_idx_ni + 1
        row_idx_new = row_idx_ni
    elif direction == "southeast":
        col_idx_new = col_idx_ni + 1
        row_idx_new = row_idx_ni + 1
    elif direction == "south":
        col_idx_new = col_idx_ni
        row_idx_new = row_idx_ni + 1
    elif direction == "southwest":
        col_idx_new = col_idx_ni - 1
        row_idx_new = row_idx_ni + 1
    elif direction == "west":
        col_idx_new = col_idx_ni - 1
        row_idx_new = row_idx_ni
    elif direction == "northwest":
        col_idx_new = col_idx_ni - 1
        row_idx_new = row_idx_ni - 1

    if (
        col_idx_new < 0
        or col_idx_new >= len(lines[0])
        or row_idx_new < 0
        or row_idx_new >= len(lines)
    ):
        return None, None
    return col_idx_new, row_idx_new


occurences = 0


def find_xmas(direction, col_idx_fd, row_idx_fd):
    for letter in "XMAS":
        if col_idx_fd is None or row_idx_fd is None:
            return 0
        if lines[row_idx_fd][col_idx_fd] != letter:
            return 0
        col_idx_fd, row_idx_fd = get_next_idx(
            direction=direction, col_idx_ni=col_idx_fd, row_idx_ni=row_idx_fd
        )
    return 1


for col_idx in range(len(lines[0])):
    for row_idx in range(len(lines)):
        if lines[row_idx][col_idx] == "X":
            for direction in directions:
                occurences += find_xmas(direction, col_idx, row_idx)

print(occurences)
