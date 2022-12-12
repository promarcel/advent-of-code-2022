from rich import print
from dataclasses import dataclass
import math
import re


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read()
    monkeys: list[Monkey] = []
    for iteration, monkey in enumerate(input.split("\n\n")):
        lines = monkey.splitlines()
        monkeys.append(
            Monkey(
                create_datatype(lines[1]),
                lines[2].split(" = ")[1],
                create_datatype(lines[3])[0],
                (create_datatype(lines[5])[0], create_datatype(lines[4])[0]),
            )
        )
    return monkeys


@dataclass
class Monkey:
    items: list[int]
    op: str
    number: int
    targets: tuple[int, int]


def create_datatype(string):
    return list(map(int, re.findall(r'-?[0-9]+', string)))


def part_1(input):
    active = [0] * len(input)
    for rounds in range(20):
        for iteration, monkey in enumerate(input):
            for item in monkey.items:
                active[iteration] += 1
                business = eval(monkey.op.replace('old', str(item)))
                business = business // 3
                input[monkey.targets[business % monkey.number == 0]].items.append(business)
            monkey.items.clear()
    active.sort()
    return active[-1] * active[-2]


def part_2(input):
    k = math.prod(monkey.number for monkey in input)
    active = [0] * len(input)
    for rounds in range(10000):
        for iteration, monkey in enumerate(input):
            for item in monkey.items:
                active[iteration] += 1
                business = eval(monkey.op.replace('old', str(item)))
                business = business % k
                input[monkey.targets[business % monkey.number == 0]].items.append(business)
            monkey.items.clear()
    active.sort()
    return active[-1] * active[-2]


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
