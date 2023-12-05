from pathlib import Path
import re

dirpath = Path("day4")
fname = dirpath / "day4.txt"
# fname = dirpath / "day4_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

card_count = {i: 1 for i in range(250)}
valid_cards = set()

total = 0
for line in lines:
    line = line.replace("\n", "")
    _, sets = line.split(":")

    card = int(re.search(r"\d+", _).group(0))
    cur_count = card_count[card]
    valid_cards.add(card)

    winning, gotten = sets.split("|")
    winning = [int(n) for n in winning.split(" ") if n != ""]
    gotten = [int(n) for n in gotten.split(" ") if n != ""]

    winning = set(winning)
    gotten = set(gotten)

    intersect = set.intersection(winning, gotten)
    for i in range(len(intersect)):
        card2 = card + 1 + i
        card_count[card2] = card_count.get(card2, 0) + cur_count

total = 0
for card in valid_cards:
    total += card_count[card]

print(total)
