from rich import print


def get_input():
    with open("input.txt") as input_txt:
        input_stacks, input_instructions = input_txt.read().split("\n\n")
    instructions = []
    for line in input_instructions.split("\n"):
        instructions.append([int(character) for character in line.split(" ") if character.isnumeric()])
    indicators = input_stacks.split("\n")[-1]
    values = input_stacks.split("\n")[-2::-1]
    stacks = []
    for indicator in range(len(indicators)):
        if indicators[indicator].isnumeric():
            stack = ""
            for line in values:
                stack += line[int(indicator)]
            stacks.append(list(stack.strip()))
    return [stacks, instructions]


def part_1(input):
    input_stacks, input_instructions = input
    stacks = [stack.copy() for stack in input_stacks]

    for instruction in input_instructions:
        movement = instruction[0]
        original = instruction[1]-1
        new = instruction[2]-1
        for _ in range(movement):
            stacks[new].append(stacks[original].pop())

    return "".join([stack[-1] for stack in stacks])


def part_2(input):
    input_stacks, input_instructions = input
    stacks = [stack.copy() for stack in input_stacks]

    for instruction in input_instructions:
        movement = instruction[0]
        original = instruction[1] - 1
        new = instruction[2] - 1
        stacks[new].extend(stacks[original][-movement:])
        stacks[original] = stacks[original][:-movement]

    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
