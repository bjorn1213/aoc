from pathlib import Path

dirpath = Path("day11")
fname = dirpath / "day11.txt"
# fname = dirpath / "day11_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]


class Stone:
    def __init__(self, iteration, value):
        self.iteration = iteration
        self.value = value

    def stone_count(self):
        if self.iteration == 75:
            return 1
        else:
            stones = self.evolve()
            score = 0
            for stone in stones:
                score += stone.stone_count()
            return score

    def evolve(self):
        strval = str(self.value)
        if self.value == 0:
            return [Stone(iteration=self.iteration + 1, value=1)]
        elif len(strval) % 2 == 0:
            return [
                Stone(
                    iteration=self.iteration + 1, value=int(strval[: len(strval) // 2])
                ),
                Stone(
                    iteration=self.iteration + 1, value=int(strval[len(strval) // 2 :])
                ),
            ]
        else:
            return [Stone(iteration=self.iteration + 1, value=self.value * 2024)]


stones = [Stone(iteration=0, value=int(l)) for l in lines[0].split(" ")]

score = 0
for stone in stones:
    score += stone.stone_count()
print(score)
