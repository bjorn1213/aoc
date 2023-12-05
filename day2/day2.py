import re

fname = "day2.txt"
# fname = "day2small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def get_colour_amount(s, colour):
    m = re.search(r"(\d+) " + colour, s)
    if m:
        return int(m.group(1))
    else:
        return 0


def add_tuples(t1, t2):
    assert len(t1) == len(t2)

    res_list = []
    for a, b in zip(t1, t2):
        res_list.append(a + b)
    return tuple(res_list)


def validate_game(subsets):
    TRUE_CONTENTS = (12, 13, 14)

    for subset in subsets:
        for i in range(len(TRUE_CONTENTS)):
            if TRUE_CONTENTS[i] < subset[i]:
                return False
        if sum(subset) > sum(TRUE_CONTENTS):
            return False
    return True


def get_min_power(subsets):
    r = []
    for a in zip(*subsets):
        r.append(max(a))

    power = 1
    for b in r:
        power *= int(b)
    return power


total = 0
for line in lines:
    m = re.match(r"Game (\d+):", line)
    assert m
    gameID = int(m.group(1))
    shows = line[m.end(0) :].replace("\n", "").split(";")

    parsed = []
    for s in shows:
        r = get_colour_amount(s, "red")
        g = get_colour_amount(s, "green")
        b = get_colour_amount(s, "blue")
        parsed.append((r, g, b))

    if validate_game(parsed):
        total += gameID
print(total)

total = 0
for line in lines:
    m = re.match(r"Game (\d+):", line)
    assert m
    gameID = int(m.group(1))
    shows = line[m.end(0) :].replace("\n", "").split(";")

    parsed = []
    for s in shows:
        r = get_colour_amount(s, "red")
        g = get_colour_amount(s, "green")
        b = get_colour_amount(s, "blue")
        parsed.append((r, g, b))

    total += get_min_power(parsed)
print(total)
