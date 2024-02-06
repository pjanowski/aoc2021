import pathlib
import pytest
import sys, os
# print(sys.path)
# print(os.getcwd())
# from ..src import day1
sys.path.append('/home/pawelrc/code/aoc2023')
import src.day1 as s

# PUZZLE_DIR = pathlib.Path("test_inputs")

# @pytest.fixture
# def data1():
#     puzzle_input = (PUZZLE_DIR / "test_input_3.txt").read_text().strip().splitlines()
#     return s.parse(puzzle_input)

TEST_INPUT = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

@pytest.fixture
def data():
    d=TEST_INPUT.strip().splitlines()
    # print(sys.path)
    # print(os.getcwd())
    return s.parse(d)

def test_solution1(data, answer=142):
    assert s.part1(data) == answer


def test_solution2(data, answer=281):
    assert s.part2(data) == answer