from pathlib import Path

dirpath = Path("day5")
fname = dirpath / "day5.txt"
# fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def process_rule(line):
    rule = tuple(int(p) for p in line.split("|"))
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


def fix_it(update, rules):
    rule_subset = [r for r in rules if r[0] in update and r[1] in update]

    while not is_valid(update, rules):
        for rule in rule_subset:
            page_first, page_last = rule
            if update[page_first] > update[page_last]:
                update[page_first], update[page_last] = (
                    update[page_last],
                    update[page_first],
                )
                break
    del update["middle"]
    arr = [a for a in sorted(update, key=lambda x: update[x])]
    return arr[len(arr) // 2]


score = 0

for update in updates:
    b = is_valid(update, rules)
    if not b:
        score += fix_it(update, rules)
    # print(b, update["middle"])

print(score)
