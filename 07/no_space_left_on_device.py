from rich import print
from collections import defaultdict


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def process(input):
    space = defaultdict(lambda: 0)
    iteration = 1
    commands = ['']
    while True:
        line = input[iteration]
        if line.startswith('$'):
            match line.split()[1:]:
                case ['cd', '..']:
                    commands.pop()
                    iteration += 1
                case ['cd', r]:
                    commands.append(r)
                    iteration += 1
                case ['ls']:
                    iterations = iteration + 1
                    while iterations < len(input):
                        k = input[iterations]
                        if k.startswith('$'):
                            break
                        elif not k.startswith('dir'):
                            size = int(k.split()[0])
                            for ssq in range(len(commands)):
                                space['/'.join(commands[:ssq + 1])] += size
                        iterations += 1
                    iteration = iterations
            if iteration >= len(input):
                break
    return space


def part_1(input):
    total = 0
    for _, space in process(input).items():
        if space <= 100000:
            total += space
    return total


def part_2(input):
    free_space = 70000000 - process(input)['']
    calculate_space = [
        space for k, space in process(input).items() if free_space + space >= 30000000
    ]
    return min(calculate_space)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
