from rich import print


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip().split())
    return input


scoring = {'X': 1, 'Y': 2, 'Z': 3}


def part_1(input):
    score = 0
    for line in input:
        player_one = line[0]
        player_two = line[1]
        score += scoring[player_two]
        if player_two == 'Y' and player_one == 'A' or player_two == 'Z' and player_one == 'B' or player_two == 'X' and player_one == 'C':
            score += 6
        elif player_two == 'Y' and player_one == 'B' or player_two == 'X' and player_one == 'A' or player_two == 'Z' and player_one == 'C':
            score += 3
    return score


def part_2(input):
    score = 0
    for line in input:
        player_one = line[0]
        player_two = line[1]
        if player_two == 'Y':
            score += 3
        if player_two == 'Z':
            score += 6
        if player_one == 'A':
            if player_two == 'X':
                score += 3
            elif player_two == 'Y':
                score += 1
            else:
                score += 2
        elif player_one == 'B':
            if player_two == 'X':
                score += 1
            elif player_two == 'Y':
                score += 2
            else:
                score += 3
        else:
            if player_two == 'X':
                score += 2
            elif player_two == 'Y':
                score += 3
            else:
                score += 1
    return score


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
