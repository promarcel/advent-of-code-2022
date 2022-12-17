from rich import print
from itertools import cycle


def get_input():
    with open("input.txt") as input_txt:
        input = cycle(enumerate([directions[iteration] for iteration in input_txt.read().strip()]))
    return input


directions = {'>': 1, '<': -1}
rocks = [{0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}, {1 + 2j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 0j},
         {2 + 2j, 2 + 1j, 0 + 0j, 1 + 0j, 2 + 0j}, {0 + 3j, 0 + 2j, 0 + 1j, 0 + 0j}, {0 + 0j, 0 + 1j, 1 + 0j, 1 + 1j}]


def highest(grid):
    return int(max(part.imag for part in grid))


def part_1(input):
    floor = set(x - 1j for x in range(7))
    falling_rocks = cycle(rocks)
    for iteration in range(2022):
        start = 2 + (4 + highest(floor)) * 1j
        rock = {start + part for part in next(falling_rocks)}
        while True:
            next_wind = next(input)
            new_rock = {part + next_wind[1] for part in rock}
            if not new_rock & floor and all(0 <= part.real <= 6 for part in new_rock):
                rock = new_rock
            new_rock = {part - 1j for part in rock}
            if floor & new_rock:
                floor.update(rock)
                break
            rock = new_rock
    return highest(floor) + 1


def part_2(input):
    floor = set(x - 1j for x in range(7))
    falling_rocks, last, iterations = cycle(enumerate(rocks)), {}, 1000000000000
    while iterations > 0:
        start = 2 + (4 + highest(floor)) * 1j
        rock_index, rock = next(falling_rocks)
        rock = {start + part for part in rock}
        while True:
            wind_index, next_wind = next(input)
            new_rock = {part + next_wind for part in rock}
            if not new_rock & floor and all(0 <= part.real <= 6 for part in new_rock):
                rock = new_rock
            new_rock = {part - 1j for part in rock}
            if floor & new_rock:
                floor.update(rock)
                break
            rock = new_rock
        max_y = highest(floor)
        heights = tuple(max_y - highest(part for part in floor if part.real == iteration) for iteration in range(7))
        iterations -= 1
        try:
            last_iteration, last_max_y = last[rock_index, wind_index, heights]
            floor = {part + iterations // (last_iteration - iterations) * (max_y - last_max_y) * 1j for part in floor}
            iterations %= last_iteration - iterations
        except KeyError:
            last[rock_index, wind_index, heights] = iterations, max_y
    return highest(floor) + 1


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
