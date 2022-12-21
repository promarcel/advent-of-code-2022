from rich import print
import operator


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().split("\n")
    return input


def handle_input(input):
    monkeys, known_monkeys, operations = {}, {}, {'+': operator.add, '-': operator.sub, '/': operator.floordiv,
                                                  '*': operator.mul}
    for monkey in input:
        name, needs = monkey.split(': ')
        if len(needs.split(' ')) > 1:
            first, operation, second = needs.split(' ')
            monkeys[name] = (first, second), operations[operation]
        else:
            known_monkeys[name] = int(needs)
    return monkeys, known_monkeys


def find_monkeys(monkeys, known_monkeys):
    find = 'root'
    while find not in known_monkeys:
        delete = []
        for monkey, (needs, operation) in monkeys.items():
            first, second = needs
            if first in known_monkeys and second in known_monkeys:
                known_monkeys[monkey] = operation(known_monkeys[first], known_monkeys[second])
                delete.append(monkey)
        for monkey in delete:
            del monkeys[monkey]
    return known_monkeys[find]


def part_1(input):
    monkeys, known_monkeys = handle_input(input)
    return find_monkeys(monkeys, known_monkeys)


def part_2(input):
    monkeys, known_monkeys = handle_input(input)
    found, previous_found, total = 1, 0, 10000000000000
    start, stop = 0, total
    iteration = (stop - start) // 1000
    human = None
    while human is None:
        for index in range(start, stop, iteration):
            previous_found = found
            known_monkeys['humn'] = index
            monkeys['root'] = (monkeys['root'][0], operator.sub)
            if (found := find_monkeys(monkeys.copy(), known_monkeys.copy())) == 0:
                human = index
                break
            if found < 0:
                start = index - iteration
                total //= 10
                stop = start + total
                iteration = (stop - start) // 1000
                found = find_monkeys(monkeys.copy(), known_monkeys.copy())
                break
    return human


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
