import pathlib
import pytest
import sys, os
# print(sys.path)
# print(os.getcwd())
# from ..src import day1
sys.path.append('/home/pawelrc/code/aoc2023')
import src.day5 as s

# PUZZLE_DIR = pathlib.Path("test_inputs")

# @pytest.fixture
# def data1():
#     puzzle_input = (PUZZLE_DIR / "test_input_3.txt").read_text().strip().splitlines()
#     return s.parse(puzzle_input)

TEST_INPUT = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

@pytest.fixture
def data():
    d=TEST_INPUT
    # print(sys.path)
    # print(os.getcwd())
    return s.parse(d)

def test_solution1(data, answer=142):
    assert s.part1(data) == answer


def test_solution2(data, answer=46):
    assert s.part2(data) == answer