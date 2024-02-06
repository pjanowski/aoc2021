# import pathlib
import sys
from aocd.models import Puzzle
import re
import multiprocessing as mp

DAY = 5

def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    # print(len(puzzle_input))
    return puzzle_input

def part1(data):
    """Solve part 1"""

    # data = data.splitlines()
    mapping = {}
    for i in range(0, len(data),1):
        if not data[i]:
            continue
        elif re.match('.*seeds:', data[i]):
            seeds = data[i].split(':')[1].strip().split(' ')
            seeds = [int(i) for i in seeds]
        elif re.match('.*map', data[i]):
            source = data[i].split()[0].split('-')[0]
            destination = data[i].split()[0].split('-')[2]
            mapping[source] = [destination]
        else:
            mapping[source].append([int(j) for j in data[i].split()])
    seeds2 = []
    while seeds:
        seed = seeds.pop(0)
        range1 = seeds.pop(0)
        seeds2.append((seed, range1))
    # print(seeds2)
    minloc = sys.maxsize
    for seed, range1 in seeds2:
        print(seed, range1)
        while range1 > 0:
            # print(seed, range1) 
            target = seed
            map1 = mapping['seed']
            # print(target)
            while True:
                # print(map1[0])
                for convs in map1[1:]:
                    if target >= convs[1] and target < convs[1]+convs[2]:
                        # print(convs)
                        target = target + convs[0] - convs[1]
                        # print(target)
                        break
                if map1[0] == 'location':
                    break
                else:
                    map1 = mapping[map1[0]]
            minloc = min(minloc, target)
            # print(minloc) 
            seed += 1
            range1 -= 1
        print(minloc)
    # print(locations)
    answer = minloc
    return answer


def part2(data):
    seeds, *blocks = data.split('\n\n')
    
    seeds = list(map(int, seeds.split(':')[1].strip().split(' ')))
    seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    maps = []
    for block in blocks:
        block = block.splitlines()[1:]
        block = [list(map(int, l.split())) for l in block]
        maps.append(block)

    locations = []
    for seed in seeds:
        ranges = [seed]
        for mappings in maps:
            new = []
            for target, source, offset in mappings:
                new_ranges = []
                for s,e in ranges:
                    start = max(s, source)
                    end = min(e, source + offset)
                    if start < end:
                        new_range = (start + target - source, end + target - source)
                        new.append(new_range)
                        if start > s:
                            new_ranges.append((s, start))
                        if end < e:
                            new_ranges.append((end, e))
                    else:
                        new_ranges.append((s, e))
                ranges = new_ranges   
            new = new + ranges
            ranges = new
        locations += ranges    
    return min(locations, key=lambda x: x[0])[0]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    # solution1 = part1(data)
    solution1 = 0
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=DAY)
    puzzle_input = puzzle.input_data
    print(solve(puzzle_input))
