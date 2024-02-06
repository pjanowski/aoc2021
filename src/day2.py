# import pathlib
# import sys
from aocd.models import Puzzle
import re

DAY = 2


def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    return puzzle_input


def part1(data):
    """Solve part 1"""
    answer = 0
    bag = {'red': 12, 'green': 13, 'blue': 14}
    for l in data:
        goodgame = 1
        for color, constraint in bag.items():
            p = fr'\d+(?= {color})'
            matches = re.findall(p, l)
            matches = [1 if int(match) > constraint else 0 for match in matches]
            if sum(matches) > 0:
                goodgame = 0
                break
        if goodgame:
            game = int(re.findall(r'(?<=Game )\d+', l)[0])
            answer += game
    return answer


def part2(data):
    answer = 0
    for l in data:
        power = 1
        for color in ['red', 'green', 'blue']:
            pattern = fr'\d+(?= {color})'
            matches = re.findall(pattern, l)
            power *= max([int(match) for match in matches])
        answer += power
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
