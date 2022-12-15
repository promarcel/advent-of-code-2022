from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            line = line.strip().split('\n')[0].split(' ')
            input.append((int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])))
    return input


def part_1(input):
    row_y = 2000000
    rounds = set()
    for sensor_x, sensor_y, beacon_x, beacon_y in input:
        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        distance_y = abs(row_y - sensor_y)
        if distance_y <= distance:
            minimal_x = sensor_x - (distance - distance_y)
            maximal_x = sensor_x + (distance - distance_y)
            for distance_x in range(minimal_x, maximal_x + 1):
                if row_y == beacon_y and distance_x == beacon_x:
                    continue
                rounds.add(distance_x)
    return len(rounds)


def part_2(input):
    for row_y in range(4000001):
        rounds_intervals = []
        for sensor_x, sensor_y, beacon_x, beacon_y in input:
            distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
            distance_y = abs(row_y - sensor_y)
            if distance_y <= distance:
                minimal_x = max(sensor_x - (distance - distance_y), 0)
                maximal_x = min(sensor_x + (distance - distance_y), 4000000)
                rounds_intervals.append((minimal_x, maximal_x))
        rounds_intervals.sort()
        current, highest = -1, -1
        for minimal_x, minimal_y in rounds_intervals:
            if minimal_x > highest + 1:
                frequency = row_y + 4000000 * (current + 1)
                break
            highest = max(highest, minimal_y)
            current = minimal_y
    return frequency


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
