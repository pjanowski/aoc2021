# import pathlib
# import sys
from aocd.models import Puzzle
import re

DAY = 3


def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    # print(len(puzzle_input))
    return puzzle_input

def isnot_digit_dot(candidate):
    if candidate.isnumeric():
        return False
    if candidate == '.':
        return False
    return True

def part1(data):
    """Solve part 1"""
    answer = 0
    for i, l in enumerate(data):
        matches = [(m.start(), m.end()) for m in re.finditer(f'\d+', l)]
        for match in matches:
            start = match[0]
            end = match[1]

            if start != 0:
                candidate = data[i][start-1]
                if isnot_digit_dot(candidate):
                    answer += int(l[start:end])
                    continue

            if end != len(l):
                candidate = data[i][end]
                if isnot_digit_dot(candidate):
                    answer += int(l[start:end])
                    continue
 
            if i != 0:
                for c in range(start-1, end+1):
                    if c >= 0 and c < len(data[i-1]):
                        candidate = data[i-1][c]
                        if isnot_digit_dot(candidate):
                            answer += int(l[start:end])
                            continue

            if i != len(data)-1:
                for c in range(start-1, end+1):
                    if c >= 0 and c < len(data[i+1]):
                        candidate = data[i+1][c]
                        if isnot_digit_dot(candidate):
                            answer += int(l[start:end])
                            continue

    return answer


def part2(data):
    answer = 0
    for i in range(len(data)):
        stars = [m.start() for m in re.finditer(f'\*', data[i])]
        for star in stars:
            if star == 118:
                print(star)
            adjacent = []

            # find adjecent numbers in top row
            pos = star
            # an = True
            candidate = ''
            pos = star
            if i > 0:
                row = data[i-1]
                an = True
            else:
                an = False

            while an:
                pos = pos - 1
                if pos >= 0 and row[pos].isnumeric():
                    candidate += row[pos]
                else:
                    candidate = candidate[::-1]
                    an = False
            
            pos = star
            while pos < star + 2:
                if i > 0:
                    an = True
                while an:
                    if pos < len(row) and row[pos].isnumeric():
                        candidate += row[pos]
                    else:
                        an = False
                        if candidate != '':
                            adjacent.append(int(candidate))
                            candidate = ''
                    pos += 1

            # find adjacent numbers left
            an = True
            candidate = ''
            pos = star
            while an:
                pos = pos - 1
                if pos >= 0 and data[i][pos].isnumeric():
                    candidate += data[i][pos]
                else:
                    an = False
            if candidate != '':
                adjacent.append(int(candidate[::-1]))
                

            # find adjacent numbers right
            an = True
            candidate = ''
            pos = star
            while an:
                pos = pos + 1
                if pos < len(data[i]) and data[i][pos].isnumeric():
                    candidate += data[i][pos]
                else:
                    an = False
            if candidate != '':
                adjacent.append(int(candidate))
                # print( adjacent, data[i])
            
            # find adjacent numbers bottom row
            pos = star
            an = True
            candidate = ''
            pos = star
            row = data[i+1]
            while an:
                pos = pos - 1
                if pos >= 0 and i+1 < len(data) and row[pos].isnumeric():
                    candidate += row[pos]
                else:
                    candidate = candidate[::-1]
                    an = False
            
            pos = star
            while pos < star + 2:
                an = True
                while an:
                    if pos < len(row) and i+1 < len(data) and row[pos].isnumeric():
                        candidate += row[pos]
                    else:
                        an = False
                        if candidate != '':
                            adjacent.append(int(candidate))
                            candidate = ''
                    pos += 1

            if len(adjacent) == 2:
                answer += adjacent[0]*adjacent[1]
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
