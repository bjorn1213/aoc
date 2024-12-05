from pathlib import Path

dirpath = Path("day5")
# fname = dirpath / "day5.txt"
fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def process_rule(line):
    rule = tuple(line.split("|"))
    return rule


def process_update(line):
    pages = [int(p) for p in line.split(",")]
    update = {}
    for i, page in enumerate(pages):
        update[page] = i
        if i == len(pages) // 2:
            update["middle"] = page
    return update


reading_rules = True

rules = []
updates = []

for line in lines:
    line = line.replace("\n", "")
    if line == "":
        reading_rules = False
        continue

    if reading_rules:
        rules.append(process_rule(line))
    else:
        updates.append(process_update(line))


def is_valid(update, rules):
    for rule in rules:
        page_first, page_last = (int(p) for p in rule)
        if not (rule[0] in update and rule[1] in update):
            continue
        if update[page_last] < update[page_first]:
            return False
    return True


score = 0

for update in updates:
    if is_valid(update, rules):
        score += 1

print(score)
