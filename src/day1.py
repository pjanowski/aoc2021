# import pathlib
# import sys
from aocd.models import Puzzle
import re

DAY = 1


def parse(puzzle_input):
  """Parse input"""
  # print(puzzle_input)
  return puzzle_input


def part1(data):
  """Solve part 1"""
  answer = 0
  for l in data:
    digits = re.findall(r'\d', l)
    number = int(''.join([digits[0], digits[-1]]))
    answer += number
    # print (l, number, answer)
  return answer


def part2(data):
    answer = 0
    translate = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
      'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    pattern = r'\d|one|two|three|four|five|six|seven|eight|nine|zero'
    for l in data:
        matches = re.finditer(f'(?=({pattern}))', l)
        digits = [match.group(1) for match in matches]
        first = translate[digits[0]] if digits[0] in translate else digits[0]
        last = translate[digits[-1]] if digits[-1] in translate else digits[-1]
        number = int(''.join([first, last]))
        answer += number
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
