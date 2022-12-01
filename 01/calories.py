from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def calculate(input):
    elves = []
    index = 0
    for line in input:
        if not line:
            elves.append(index)
            index = 0
            continue
        index += int(line)
    elves.append(index)
    return elves


def part_1(input):
    return max(calculate(input))


def part_2(input):
    elves = calculate(input)
    elves.sort()
    return sum(elves[-3:])


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
