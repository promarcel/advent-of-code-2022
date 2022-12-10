from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip().split())
    return input


def determine_position(input, result_index):
    knot_a, knot_b, rope = {(0, 0)}, {(0, 0)}, [(0, 0)] * 10
    moves = {"D": [0, 1], "R": [1, 0], "U": [0, -1], "L": [-1, 0]}
    for iteration in [step for step in input]:
        for _ in range(int(iteration[1])):
            rope[0] = (rope[0][0] + moves[iteration[0]][0], rope[0][1] + moves[iteration[0]][1])
            for tail in range(1, len(rope)):
                x = rope[tail - 1][0] - rope[tail][0]
                y = rope[tail - 1][1] - rope[tail][1]
                if x == 0 and abs(y) > 1:
                    rope[tail] = (rope[tail][0], rope[tail][1] + (1 if y > 0 else -1))
                elif abs(x) > 1 and y == 0:
                    rope[tail] = (rope[tail][0] + (1 if x > 0 else -1), rope[tail][1])
                elif x <= -1 and y == -2 or x == -2 and y <= -1:
                    rope[tail] = (rope[tail][0] - 1, rope[tail][1] - 1)
                elif x >= 1 and y == -2 or x == 2 and y <= -1:
                    rope[tail] = (rope[tail][0] + 1, rope[tail][1] - 1)
                elif x <= -1 and y == 2 or x == -2 and y >= 1:
                    rope[tail] = (rope[tail][0] - 1, rope[tail][1] + 1)
                elif x >= 1 and y == 2 or x == 2 and y >= 1:
                    rope[tail] = (rope[tail][0] + 1, rope[tail][1] + 1)
                knot_a.add(rope[1])
                knot_b.add(rope[9])
    return len(eval(result_index))


def part_1(input):
    return determine_position(input, "knot_a")


def part_2(input):
    return determine_position(input, "knot_b")


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
