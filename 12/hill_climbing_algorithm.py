from rich import print
import itertools
import heapq
from string import ascii_lowercase
from collections import defaultdict


def get_input():
    input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            input.append(line.strip())
    return input


def neighbors(G, r, c, height, width):
    for dx in [-1, 1]:
        if 0 <= (j := r + dx) < height:
            yield j, c
        if 0 <= (k := c + dx) < width:
            yield r, k


def calculate(input, start, end, height, width):
    def height(j, k):
        return abs(j - end[0]) + abs(k - end[1])

    min_steps = {(input, start): 0}
    g_score = defaultdict(lambda: float('inf'))
    g_score[input, start] = 0
    f_score = defaultdict(lambda: float('inf'))
    f_score[input, start] = 0 + height(input, start)
    open_set = [(f_score[input, start], (input, start))]

    while len(open_set) > 0:
        cost, curr = heapq.heappop(open_set)
        node = input[curr[0]][curr[1]]
        if node == target:
            return min_steps[curr]
        for j, k in neighbors(input, *curr, height, width):
            new_elev = elev[input[j][k]]
            curr_elev = elev[node]
            d = 1 if new_elev - curr_elev <= 1 else float('inf')
            score = g_score[curr] + d
            if score < g_score[j, k]:
                min_steps[j, k] = min_steps[curr] + 1
                g_score[j, k] = score
                f_score[j, k] = score + height(j, k)
                coords = [x for _, x in open_set]
                if (j, k) not in coords:
                    heapq.heappush(open_set, (f_score[j, k], (j, k)))
    return -1


start = 'S'
target = 'E'
elev = {k: i for i, k in enumerate(ascii_lowercase)}
elev['S'] = 0
elev['E'] = 25


def part_1(input):
    height = len(input)
    width = len(input[0])

    start = next((r, c) for r, c in itertools.product(
        range(height), range(width)) if input[r][c] == start)
    end = next((r, c) for r, c in itertools.product(
        range(height), range(width)) if input[r][c] == target)

    return calculate(input, *start, end, height, width)


def part_2(input):
    H = len(input)
    W = len(input[0])

    best_signal = float('inf')
    end = next((r, c) for r, c in itertools.product(
        range(H), range(W)) if input[r][c] == target)
    for r, c in itertools.product(range(H), range(W)):
        if input[r][c] != 'a':
            continue
        if 0 < (k := calculate(r, c, end)) < best_signal:
            best_signal = k
    return best_signal


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
