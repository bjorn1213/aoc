from pathlib import Path

dirpath = Path("day7")
fname = dirpath / "day7.txt"
# fname = dirpath / "day7_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()

values = list("abcdefghijklmnopqrstuvw")

scores = {card: values[value_idx] for value_idx, card in enumerate("J23456789TQKA")}


class Hand:
    def __init__(self, hand, bid=0):
        self.hand_original = hand
        self.hand = "".join([scores[card] for card in hand])

        freq = {card: 0 for card in hand}
        for card in hand:
            freq[card] += 1
        hand_class_original = sorted(list(freq.values()), reverse=True)
        hand_class_original = hand_class_original + [0] * (5 - len(hand_class_original))

        freq = {card: 0 for card in hand if card != "J"}
        jokers = 0
        for card in hand:
            if card == "J":
                jokers += 1
                continue
            freq[card] += 1

        freq = sorted(list(freq.values()), reverse=True)
        freq = freq + [0] * (5 - len(freq))
        for _ in range(jokers):
            for i, f in enumerate(freq):
                if f < 5:
                    freq[i] += 1
                    break

        self.full_hand = "".join(
            [str(a) for a in freq]
            # + [str(a) for a in hand_class_original]
            + list(self.hand)
        )

        self.bid = bid

    def __lt__(self, other):
        return self.full_hand < other.full_hand

    def __repr__(self):
        return self.hand_original

    def get_winnings(self, rank):
        return self.bid * rank


hands = []
for line in lines:
    l = line.replace("\n", "")
    hand, bid = l.split(" ")
    hands.append(Hand(hand, int(bid)))

total = 0
for hand, rank in zip(sorted(hands), range(1, len(hands) + 1)):
    total += hand.get_winnings(rank)
    print(hand, rank, hand.get_winnings(rank))

print(total)

# Hand("JJJJJ")
