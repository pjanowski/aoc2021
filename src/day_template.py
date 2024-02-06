# import pathlib
# import sys
from aocd.models import Puzzle
import re

DAY = 4


def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    # print(len(puzzle_input))
    return puzzle_input

def part1(data):
    """Solve part 1"""
    answer = 0
    return answer


def part2(data):
    answer = 0

    return answer


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
