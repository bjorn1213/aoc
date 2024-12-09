from pathlib import Path

dirpath = Path("day9")
fname = dirpath / "day9.txt"
# fname = dirpath / "day9_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
line = lines[0].replace("\n", "")


max_id = (len(line) - 1) / 2

keep_going = True
total = 0
cur_idx = 0
numbers = [int(i) for i in line]
cur_file_id = 0
is_file = True
spaces_to_process = numbers.pop(0)
health_bar = numbers.pop()

while len(numbers):
    for _ in range(spaces_to_process):
        if is_file:
            number_to_add = cur_file_id * cur_idx
            total += number_to_add
        else:
            number_to_add = cur_idx * max_id
            total += number_to_add
            health_bar -= 1
            if health_bar == 0:
                max_id -= 1
                health_bar = numbers.pop()
                health_bar = numbers.pop()
        cur_idx += 1

    spaces_to_process = numbers.pop(0)
    if is_file:
        cur_file_id += 1
    is_file = not is_file

for _ in range(health_bar):
    total += cur_idx * max_id
    cur_idx += 1

print(total)
