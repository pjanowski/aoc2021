# aoc_template.py


import pathlib
import sys
from aocd.models import Puzzle

DAY = {day}

def parse(puzzle_input):
    """Parse input"""
    print(data)
    return data

def part1(data):
    """Solve part 1"""

def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=DAY)
    puzzle_input = puzzle.input_data.splitlines()
    print(solve(puzzle_input))