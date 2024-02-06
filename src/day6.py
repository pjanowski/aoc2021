# import pathlib
# import sys
from aocd.models import Puzzle
import re

DAY = 6

data1 = '''Time:      71530
Distance:  940200
'''
data1 = data1.splitlines()


def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    # print(len(puzzle_input))
    return puzzle_input


def part1(data):
    """Solve part 1"""
    ts = data[0].split(":")[1].strip().split()
    ts = list(map(int, ts))
    ds = data[1].split(":")[1].strip().split()
    ds = list(map(int, ds))

    answer = 1
    for t, record in zip(ts, ds):
        ways = 0
        for i in range(1, t):
            d = i*(t-i)
            if d > record:
                ways += 1
        print(ways)
        answer *= ways
    return answer


def part2(data):
    ts = int("".join(data[0].split(":")[1].strip().split()))
    ds = int("".join(data[1].split(":")[1].strip().split()))

    for i in range(1, ts): 
        if i*(ts-i) > ds:
            start = i
            break

    for j in range(ts, 0, -1):
        if j*(ts-j) > ds:
            end = j
            break

    return end - start + 1


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=DAY)
    puzzle_input = puzzle.input_data.splitlines()
    print(solve(puzzle_input))
