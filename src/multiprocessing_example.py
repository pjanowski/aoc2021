from multiprocessing import Pool, Value
import time
from aocd.models import Puzzle
import re

DAY = 6

def parse(puzzle_input):
    """Parse input"""
    # print(puzzle_input)
    # print(len(puzzle_input))
    return puzzle_input

ways = Value('i', 0) 

def isbetter(i, t, record):
    d = i*(t-i)
    if d > record:
        with ways.get_lock():
            ways.value = ways.value + 1
    return 0

def isbetter1(i, t, record):
    d = i*(t-i)
    if d > record:
        return 1
    return 0

def isbetter2(args):
    i = args[0]
    t = args[1]
    record = args[2]
    d = i*(t-i)
    if d > record:
        return 1
    return 0

def isbetter4(args):
    i = args[0]
    t = args[1]
    record = args[2]
    d = i*(t-i)
    if d > record:
        with ways.get_lock():
            ways.value = ways.value + 1
    return 0

def part1(data):
    """Solve part 1"""
    ts = data[0].split(":")[1].strip().split()
    ts = list(map(int, ts))
    ds = data[1].split(":")[1].strip().split()
    ds = list(map(int, ds))

    answer = 1
    for t, record in zip(ts, ds):
        pool = Pool(4)
        
        st = time.perf_counter()
        results = []
        ways.value = 0
        for i in range(1, t):
            x = pool.apply_async(isbetter, (i, t, record,))
            results.append(x)
        _ = [x.get() for x in results]
        et = time.perf_counter() - st
        print(ways.value, et)

        st = time.perf_counter()
        results = []
        for i in range(1, t):
            x = pool.apply_async(isbetter1, (i, t, record,))
            results.append(x)
        result_apply = sum([x.get() for x in results])
        et = time.perf_counter() - st
        print(result_apply, et)

        # map_async is faster than apply_async, either of the below ways, with global var or get result
        st = time.perf_counter()
        args = [[i, t, record] for i in range(1, t)]
        results = pool.map_async(isbetter2, args)
        result_map = sum(results.get())
        et = time.perf_counter() - st
        print(result_map, et)

        st = time.perf_counter()
        ways.value = 0
        args = [[i, t, record] for i in range(1, t)]
        results = pool.map_async(isbetter4, args)
        results.get()
        et = time.perf_counter() - st
        print(ways.value, et)

        pool.close()
        pool.join()

        answer *= ways.value
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
