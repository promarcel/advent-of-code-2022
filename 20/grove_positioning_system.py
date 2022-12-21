from rich import print


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().split("\n")
    return input


def decryption(input, count, decryption_key):
    query = [(int(position) * decryption_key, index) for index, position in enumerate(input)]
    clear, length = query[:], len(query)
    for _ in range(count):
        for positions in clear:
            index = query.index(positions)
            original = query.pop(index)
            new_index = (index + original[0] - 1) % (length - 1) + 1
            query.insert(new_index, original)
    result = 0
    for position, original in enumerate(query):
        if original[0] == 0:
            result = position
            break
    return sum(query[(result + i * 1000) % length][0] for i in range(1, 4))


def part_1(input):
    return decryption(input, 1, 1)


def part_2(input):
    return decryption(input, 10, 811589153)


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
