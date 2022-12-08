from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def part_1(input):
    trees = [list(map(int, list(line))) for line in input]
    rows = len(input)
    visible = set()
    for y_coordinate in range(rows):
        height = -1
        for x_coordinate in range(rows):
            if trees[x_coordinate][y_coordinate] > height:
                height = trees[x_coordinate][y_coordinate]
                visible.add((x_coordinate, y_coordinate))
        height = -1
        for x_coordinate in range(rows - 1, -1, -1):
            if trees[x_coordinate][y_coordinate] > height:
                height = trees[x_coordinate][y_coordinate]
                visible.add((x_coordinate, y_coordinate))
    for x_coordinate in range(rows):
        height = -1
        for y_coordinate in range(rows):
            if trees[x_coordinate][y_coordinate] > height:
                height = trees[x_coordinate][y_coordinate]
                visible.add((x_coordinate, y_coordinate))
        height = -1
        for y_coordinate in range(rows - 1, -1, -1):
            if trees[x_coordinate][y_coordinate] > height:
                height = trees[x_coordinate][y_coordinate]
                visible.add((x_coordinate, y_coordinate))
    return len(visible)


def part_2(input):
    trees = [list(map(int, list(line))) for line in input]
    rows = len(input)
    height = 0
    for y_coordinate in range(rows):
        for x_coordinate in range(rows):
            scenic_score = 1
            for calculate in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                base = 0
                x_calculated = x_coordinate + calculate[0]
                y_calculated = y_coordinate + calculate[1]
                while 0 <= x_calculated < rows and 0 <= y_calculated < rows:
                    base += 1
                    if trees[x_calculated][y_calculated] >= trees[x_coordinate][y_coordinate]:
                        break
                    x_calculated += calculate[0]
                    y_calculated += calculate[1]
                scenic_score *= base
            if scenic_score > height:
                height = scenic_score
    return height


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
