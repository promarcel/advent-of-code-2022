from rich import print
from functools import cmp_to_key


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().strip()
    return input


def compare_signal(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        index = 0
        while index < len(left) and index < len(right):
            compare = compare_signal(left[index], right[index])
            if compare == -1:
                return -1
            if compare == 1:
                return 1
            index += 1
        if index == len(left) and index < len(right):
            return -1
        elif index == len(right) and index < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare_signal([left], right)
    else:
        return compare_signal(left, [right])


distress_signal = []


def part_1(input):
    global distress_signal
    packets, signal = [], 0
    for index, signal_group in enumerate(input.split('\n\n')):
        left, right = signal_group.split('\n')
        left, right = eval(left), eval(right)
        packets.append(left)
        packets.append(right)
        if compare_signal(left, right) == -1:
            signal += 1 + index
    distress_signal = packets
    return signal


def part_2(input):
    global distress_signal
    distress_signal.append([[2]])
    distress_signal.append([[6]])
    packets, signal = sorted(distress_signal, key=cmp_to_key(lambda left, right: compare_signal(left, right))), 1
    for index, packets in enumerate(packets):
        if packets == [[2]] or packets == [[6]]:
            signal *= index + 1
    return signal


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
