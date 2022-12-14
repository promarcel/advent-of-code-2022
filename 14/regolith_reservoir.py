from rich import print


def get_input():
    matrix, matrix[0][500], bottom = [['.'] * 2000 for index in range(1000)], '+', 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            steps = line.strip().split()[::2]
            for start, end in zip(steps, steps[1:]):
                coordinate_y_source, coordinate_x_source = start.split(',')
                coordinate_y_destination, coodinate_y_destination = end.split(',')
                coordinate_x_source, coodinate_y_destination, coordinate_y_source, coordinate_y_destination = int(
                    coordinate_x_source), int(coodinate_y_destination), int(coordinate_y_source), int(
                    coordinate_y_destination)
                if coordinate_x_source == coodinate_y_destination:
                    x = coordinate_x_source
                    for y in range(min(coordinate_y_source, coordinate_y_destination),
                                   max(coordinate_y_source, coordinate_y_destination) + 1):
                        matrix[x][y] = '#'
                if coordinate_y_source == coordinate_y_destination:
                    y = coordinate_y_source
                    for x in range(min(coordinate_x_source, coodinate_y_destination),
                                   max(coordinate_x_source, coodinate_y_destination) + 1):
                        matrix[x][y] = '#'
                if matrix[x][y] == '#':
                    bottom = max(bottom, x)
    return matrix, bottom


def part_1(input):
    matrix, bottom = input
    coordinate_x, coordinate_y, sand = 0, 500, 0
    while coordinate_x <= bottom:
        if matrix[coordinate_x + 1][coordinate_y] == '.' or matrix[coordinate_x + 1][coordinate_y - 1] == '.' or \
                matrix[coordinate_x + 1][coordinate_y + 1] == '.':
            if matrix[coordinate_x + 1][coordinate_y] == '.':
                ...
            elif matrix[coordinate_x + 1][coordinate_y - 1] == '.':
                coordinate_y -= 1
            else:
                coordinate_y += 1
            coordinate_x += 1
        else:
            sand += 1
            matrix[coordinate_x][coordinate_y] = 'o'
            coordinate_x, coordinate_y = 0, 500
    coordinate_x, coordinate_y = 0, 500
    while coordinate_x <= bottom + 3:
        if matrix[coordinate_x + 1][coordinate_y] == '.' or matrix[coordinate_x + 1][coordinate_y - 1] == '.' or \
                matrix[coordinate_x + 1][coordinate_y + 1] == '.':
            if matrix[coordinate_x + 1][coordinate_y] == '.':
                ...
            elif matrix[coordinate_x + 1][coordinate_y - 1] == '.':
                coordinate_y -= 1
            else:
                coordinate_y += 1
            coordinate_x += 1
            matrix[coordinate_x][coordinate_y] = '~'
    return sand


def part_2(input):
    matrix, bottom = input
    for iteration in range(len(matrix[0])):
        matrix[bottom][iteration] = '#'
    coordinate_x, coordinate_y, sand = 0, 500, 0
    while coordinate_x <= bottom:
        if matrix[coordinate_x + 1][coordinate_y] == '.' or matrix[coordinate_x + 1][coordinate_y - 1] == '.' or \
                matrix[coordinate_x + 1][coordinate_y + 1] == '.':
            if matrix[coordinate_x + 1][coordinate_y] == '.':
                ...
            elif matrix[coordinate_x + 1][coordinate_y - 1] == '.':
                coordinate_y -= 1
            else:
                coordinate_y += 1
            coordinate_x += 1
        else:
            sand += 1
            matrix[coordinate_x][coordinate_y] = 'o'
            if coordinate_x == 0 and coordinate_y == 500:
                break
            coordinate_x, coordinate_y = 0, 500
    return sand


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
