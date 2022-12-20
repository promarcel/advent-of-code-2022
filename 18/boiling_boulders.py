from rich import print
import numpy
import fill_voids


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().splitlines()
    return [[int(number) for number in line.split(',')] for line in input]


def neighboor(position):
    calculate = []
    calculate.append([position[0] + 1, position[1], position[2]])
    calculate.append([position[0], position[1] + 1, position[2]])
    calculate.append([position[0], position[1], position[2] + 1])
    calculate.append([position[0] - 1, position[1], position[2]])
    calculate.append([position[0], position[1] - 1, position[2]])
    calculate.append([position[0], position[1], position[2] - 1])
    calculate = [coordinate for coordinate in calculate if
                 not (coordinate[0] < 0 or coordinate[1] < 0 or coordinate[2] < 0)]
    return calculate


def part_1(input):
    count = []
    for coordinates in input:
        positions = sum([1 for number in neighboor(coordinates) if number in input])
        count.append(positions)
    return sum([6 - number for number in count])


def part_2(input):
    coordinates = numpy.array(input)
    x, y, z = coordinates[:, 0].max(), coordinates[:, 1].max(), coordinates[:, 2].max()
    system = numpy.zeros((x + 1, y + 1, z + 1))
    for position in coordinates:
        system[position[0], position[1], position[2]] = 1
    infill = fill_voids.fill(system, in_place=False)
    input = numpy.vstack((numpy.where(infill == 1))).T
    input = [list(coordinates) for coordinates in input]
    return part_1(input)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
