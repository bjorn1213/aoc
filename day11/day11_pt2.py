from pathlib import Path
from collections import Counter

dirpath = Path("day11")
fname = dirpath / "day11.txt"
# fname = dirpath / "day11_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

freqs = {}


class Stone:
    def __init__(self, iteration, value, stop_iteration):
        self.iteration = iteration
        self.value = value
        self.stop_iteration = stop_iteration
        self.freqs = Counter()

    def stone_count(self):
        self.freqs = Counter()
        if self.iteration == self.stop_iteration:
            return Counter({self.value: 1})
        else:
            stones = self.evolve()
            for stone in stones:
                stone_freqs = stone.stone_count()
                self.freqs = self.freqs + stone_freqs
            return self.freqs

    def evolve(self):
        strval = str(self.value)
        if self.value == 0:
            return [
                Stone(
                    iteration=self.iteration + 1,
                    value=1,
                    stop_iteration=self.stop_iteration,
                )
            ]
        elif len(strval) % 2 == 0:
            return [
                Stone(
                    iteration=self.iteration + 1,
                    value=int(strval[: len(strval) // 2]),
                    stop_iteration=self.stop_iteration,
                ),
                Stone(
                    iteration=self.iteration + 1,
                    value=int(strval[len(strval) // 2 :]),
                    stop_iteration=self.stop_iteration,
                ),
            ]
        else:
            return [
                Stone(
                    iteration=self.iteration + 1,
                    value=self.value * 2024,
                    stop_iteration=self.stop_iteration,
                )
            ]


stones = [
    Stone(iteration=0, value=int(l), stop_iteration=25) for l in lines[0].split(" ")
]

stone_counts = Counter()
for stone in stones:
    stone_counts[stone.value] = stone_counts.get(stone.value, 0) + 1


def get_five_map(value):
    return Stone(iteration=0, value=value, stop_iteration=5).stone_count()


five_maps = {}

ITERATION_COUNT = 75

for i in range(ITERATION_COUNT // 5):
    print(i)
    stone_counts
    updated_stone_counts = Counter()

    for stone, stone_amount in stone_counts.items():
        if stone not in five_maps:
            five_map = get_five_map(stone)
            five_maps[stone] = five_map
        updated_stone_counts = updated_stone_counts + Counter(
            {k: v * stone_amount for k, v in five_maps[stone].items()}
        )
    stone_counts = updated_stone_counts

score = 0
for v in stone_counts.values():
    score += v
print(score)
