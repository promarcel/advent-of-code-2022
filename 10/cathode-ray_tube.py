from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip().split())
    return input


def part_1(input):
    value, signal, index = 1, 0, -1
    for command in input:
        if command[0] == 'noop':
            index += 1
            if index + 1 == 20 or index + 1 == 60 or index + 1 == 100 or index + 1 == 140 or index + 1 == 180 or index + 1 == 220:
                signal += (index + 1) * value
        elif command[0] == 'addx':
            index += 1
            if index + 1 == 20 or index + 1 == 60 or index + 1 == 100 or index + 1 == 140 or index + 1 == 180 or index + 1 == 220:
                signal += (index + 1) * value
            index += 1
            if index + 1 == 20 or index + 1 == 60 or index + 1 == 100 or index + 1 == 140 or index + 1 == 180 or index + 1 == 220:
                signal += (index + 1) * value
            value += int(command[1])
    return signal


def part_2(input):
    value, signal, index = 1, 0, -1
    picture = {value - 1, value, value + 1}
    image = [[' ' for i in range(40)] for n in range(6)]
    printer = '\n'

    def paint(index):
        if index % 40 in picture:
            image[index // 40][index % 40] = '█'
        else:
            image[index // 40][index % 40] = ' '

    for command in input:
        if command[0] == 'noop':
            index += 1
            paint(index)
        elif command[0] == 'addx':
            index += 1
            paint(index)
            index += 1
            paint(index)
            value += int(command[1])
            picture = {value - 1, value, value + 1}
    for line in image:
        printer += ''.join(line) + '\n'
    return printer


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
