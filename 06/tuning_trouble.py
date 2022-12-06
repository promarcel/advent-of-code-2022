from rich import print


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read()
    return input


def part_1(input):
    for character in range(0, len(input)):
        iterate = False
        for check_marker in range(character, character + 3):
            for marker in range(check_marker + 1, character + 4):
                if input[check_marker] == input[marker]:
                    iterate = True
                    break
            if iterate:
                break
        if not iterate:
            result = str(character + 4)
            break
    return result


def part_2(input):
    for character in range(0, len(input)):
        iterate = False
        for check_marker in range(character, character + 13):
            for marker in range(check_marker + 1, character + 14):
                if input[check_marker] == input[marker]:
                    iterate = True
                    break
            if iterate:
                break
        if not iterate:
            result = str(character + 14)
            break
    return result


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
