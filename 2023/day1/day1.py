import re

fname = "day1.txt"
# fname = "day1_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

d = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern = r"[123456789]|" + "|".join([k for k in d.keys()])

total = 0
for line in lines:
    leftover = line

    matches = []

    while len(leftover) > 0:
        m = re.search(pattern, leftover)
        if m:
            matches.append(m.group(0))
            leftover = leftover[1:]
        else:
            break
    parsed = [d.get(m, m) for m in matches]
    str_val = parsed[0] + parsed[-1]
    total += int(str_val)

print(total)
