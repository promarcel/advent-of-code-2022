from rich import print
import re


def get_input():
    with open("input.txt") as input_txt:
        input = input_txt.read().split("\n")
    return input


def check_items(line, count):
    blueprint, ore_robot, clay_robot, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, \
        geode_robot_obsidian = map(int, re.findall(r'\d+', line))
    costs = (ore_robot, 0, 0, 0), (clay_robot, 0, 0, 0), (obsidian_robot_ore, obsidian_robot_clay, 0, 0), (
        geode_robot_ore, 0, geode_robot_obsidian, 0)
    marks = (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
    seen = {}
    initial_robots = 1, 0, 0, 0
    initial_resources = 0, 0, 0, 0
    minute_passed = 0
    stack = [(initial_robots, initial_resources, minute_passed)]
    max_geode = 0
    while stack:
        robots, res, material = stack.pop()
        if (robots, res) in seen and seen[(robots, res)] <= material:
            continue
        seen[(robots, res)] = material
        if material == count:
            max_geode = max(max_geode, res[3])
            continue
        if (count - material) * robots[3] + res[3] + (count - material) * (count - 1 - material) / 2 < max_geode:
            continue
        stack.append((robots, tuple(resource + rs for resource, rs in zip(robots, res)), material + 1))
        for i in range(4):
            if i != 3 and robots[i] >= max(cost[i] for cost in costs):
                continue
            if all(resource >= count for count, resource in zip(costs[i], res)):
                stack.append((tuple(resource + material for resource, material in zip(robots, marks[i])),
                              tuple(resource + resource_stack - count for resource, resource_stack, count in
                                    zip(robots, res, costs[i])), material + 1))
    return max_geode, blueprint


def part_1(input):
    result = 0
    for line in input:
        max_geode, blueprint = check_items(line, 24)
        result += max_geode * blueprint
    return result


def part_2(input):
    result = 1
    for line in input:
        max_geode, blueprint = check_items(line, 24)
        if blueprint < 4:
            max_geode, _ = check_items(line, 32)
            result *= max_geode
    return result


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
