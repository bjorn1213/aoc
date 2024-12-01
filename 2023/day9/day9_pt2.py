from pathlib import Path

dirpath = Path("day9")
fname = dirpath / "day9.txt"
# fname = dirpath / "day9_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def next_in_seq(seq):
    if all(s == 0 for s in seq):
        return 0
    return seq[0] - next_in_seq([a - b for a, b in zip(seq[1:], seq[:-1])])


total = 0
for line in lines:
    l = line.replace("\n", "")
    seq = [int(n) for n in l.split(" ")]
    total += next_in_seq(seq)

print(total)
