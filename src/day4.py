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
    for i in data:
        a, b = i.split('|')
        a = [int(n) for n in a.split(':')[1].strip().split()]
        b = [int(n) for n in b.strip().split()]
        match = len([n for n in b if n in a])
        if match > 0:
            points = 2**(match-1)
        else:
            points = 0
        answer += points
        # print(match, points)

    return answer


def part2(data):
    answer = 0
    copies = [1]*len(data)
    for i,row in enumerate(data):
        a, b = row.split('|')
        a = [int(n) for n in a.split(':')[1].strip().split()]
        b = [int(n) for n in b.strip().split()]
        match = len([n for n in b if n in a])    
        this_row_copies = copies[i]
        copies[i+1:i+1+match] = [c+this_row_copies for c in copies[i+1:i+1+match]]

    return sum(copies)


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
