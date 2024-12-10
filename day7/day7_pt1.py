from pathlib import Path
import re

dirpath = Path("day7")
fname = dirpath / "day7.txt"
# fname = dirpath / "day7_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()
lines = [l.replace("\n", "") for l in lines]

equations = []

for line in lines:
    target, numbers = line.split(":")
    numbers = re.findall(r"(\d+)", numbers)

    equation = {"target": int(target), "numbers": [int(n) for n in numbers]}
    equations.append(equation)


def test_equation(target: int, cur_value: int, numbers: list[int]):
    if len(numbers) == 1:
        return (cur_value + numbers[-1] == target) or (
            cur_value * numbers[-1] == target
        )

    if cur_value + sum(numbers) > target:
        return False

    return test_equation(target, cur_value + numbers[0], numbers[1:]) or test_equation(
        target, cur_value * numbers[0], numbers[1:]
    )


score = 0
for equation in equations:
    target = equation["target"]
    numbers = equation["numbers"]

    test_result = test_equation(target, numbers[0], numbers[1:])
    # print(f"{target}: {test_result}")
    if test_result:
        score += target
print(score)
