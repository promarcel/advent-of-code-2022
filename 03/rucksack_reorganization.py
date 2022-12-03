from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def part_1(input):
    priorities = 0
    for line in input:
        length = len(line)
        first = line[:length // 2]
        last = line[length // 2:]
        first_rucksack = set(list(first))
        second_rucksack = set(list(last))
        intersections = first_rucksack.intersection(second_rucksack)
        for intersection in intersections:
            if intersection.islower():
                priorities += ord(intersection) - ord('a')
            else:
                priorities += ord(intersection) - ord('A') + 26
        priorities += 1
    return priorities


def part_2(input):
    priorities = 0
    intersections = set()
    for index, line in enumerate(input):
        if len(intersections) == 0:
            intersections = set(list(line))
        else:
            intersections = intersections.intersection(set(list(line)))
            if index % 3 == 2:
                for intersection in intersections:
                    if intersection.islower():
                        priorities += ord(intersection) - ord('a')
                    else:
                        priorities += ord(intersection) - ord('A') + 26
                priorities += 1
                intersections = set()
    return priorities


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
