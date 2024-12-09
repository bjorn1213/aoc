from pathlib import Path

dirpath = Path("day9")
fname = dirpath / "day9.txt"
# fname = dirpath / "day9_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
line = lines[0].replace("\n", "")
line = [int(l) for l in line]


class Block:
    def __init__(self, size, is_file, id=None):
        self.size = size
        self.is_file = is_file
        self.id = id

    def __len__(self):
        return self.size

    def __eq__(self, other):
        self.id == other.id


def calc_block_list_score(block_list):
    total = 0
    cur_idx = 0
    for b in block_list:
        for _ in range(b.size):
            if b.is_file:
                total += b.id * cur_idx
            cur_idx += 1
    return total


def print_block_list(block_list):
    block_str = ""
    for block in block_list:
        for _ in range(block.size):
            if block.is_file:
                block_str += str(block.id)
            else:
                block_str += "."
    print(block_str)


cur_id = 0
space = []
for i, b in enumerate(line):
    if i % 2 == 0:
        space.append(Block(b, True, cur_id))
        cur_id += 1
    else:
        space.append(Block(b, False))

space_copy = [b for b in space]
offset = 0
for i, b in enumerate(space_copy[::-1]):
    if not b.is_file:
        continue
    original_index = len(space) - i

    for idx in range(space.index(b)):
        if space[idx].is_file:
            continue
        if space[idx].size >= b.size:
            space[idx].size -= b.size
            space.insert(idx, Block(b.size, True, b.id))
            b.is_file = False
            offset += 1
            break

total = calc_block_list_score(space)
print(total)
