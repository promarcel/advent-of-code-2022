from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def part_1(input):
    count = 0
    for line in input:
        elves = line.split(',')
        start_one, end_one = tuple(int(section) for section in elves[0].split('-'))
        start_two, end_two = tuple(int(section) for section in elves[1].split('-'))
        if start_one <= start_two and end_one >= end_two or start_two <= start_one and end_two >= end_one:
            count += 1
    return count


def part_2(input):
    count = 0
    for line in input:
        elves = line.split(',')
        start_one, end_one = tuple(int(section) for section in elves[0].split('-'))
        start_two, end_two = tuple(int(section) for section in elves[1].split('-'))
        if not (start_one < start_two and end_one < start_two or start_two < start_one and end_two < start_one):
            count += 1
    return count


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
