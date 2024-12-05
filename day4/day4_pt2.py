from pathlib import Path

dirpath = Path("day4")
fname = dirpath / "day4.txt"
# fname = dirpath / "day4_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]


occurences = 0


def find_x_mas(col_idx, row_idx):
    left_top = lines[row_idx - 1][col_idx - 1]
    right_top = lines[row_idx - 1][col_idx + 1]
    left_bottom = lines[row_idx + 1][col_idx - 1]
    right_bottom = lines[row_idx + 1][col_idx + 1]

    diagonal_letters = left_top + right_top + right_bottom + left_bottom
    if diagonal_letters in ("MMSS", "MSSM", "SSMM", "SMMS"):
        return 1
    return 0


for col_idx in range(1, len(lines[0]) - 1):
    for row_idx in range(1, len(lines) - 1):
        if lines[row_idx][col_idx] == "A":
            occurences += find_x_mas(col_idx=col_idx, row_idx=row_idx)

print(occurences)
