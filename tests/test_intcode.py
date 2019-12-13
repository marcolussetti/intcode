from intcode.intcode import intcode, chain_intercodes, looping_intcodes
from collections import defaultdict


# Day 2
def test_day2_part1_examples():
    assert intcode([1, 0, 0, 0, 99])[1] == defaultdict(int, enumerate([2, 0, 0, 0, 99]))
    assert intcode([2, 3, 0, 3, 99])[1] == defaultdict(int, enumerate([2, 3, 0, 6, 99]))
    assert intcode([2, 4, 4, 5, 99, 0])[1] == defaultdict(int, enumerate([2, 4, 4, 5, 99, 9801]))
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])[
        1] == defaultdict(int, enumerate([30, 1, 1, 4, 2, 5, 6, 0, 99]))


def test_day2_part1():
    with open('tests/inputs/02_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    input_lines[1] = 12
    input_lines[2] = 2
    assert intcode(input_lines)[1][0] == 4690667


def test_day2_part2():
    with open('tests/inputs/02_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    input_lines[1] = 62
    input_lines[2] = 55
    assert intcode(input_lines)[1][0] == 19690720


# Day 5
def test_day5_part1():
    with open('tests/inputs/05_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert intcode(input_lines, [1])[0][-1] == 15386262


def test_day5_part2_examples():
    assert intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8])[0][-1] == 1
    assert intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [9])[0][-1] == 0

    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7])[0][-1] == 1
    assert intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8])[0][-1] == 0

    assert intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], [7])[0][-1] == 0
    assert intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8])[0][-1] == 1

    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], [7])[0][-1] == 1
    assert intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], [8])[0][-1] == 0

    assert intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4,
                    13, 99, -1, 0, 1, 9], [0])[0][-1] == 0
    assert intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4,
                    13, 99, -1, 0, 1, 9], [7])[0][-1] == 1

    assert intcode([3, 3, 1105, -1, 9, 1101, 0, 0,
                    12, 4, 12, 99, 1], [0])[0][-1] == 0
    assert intcode([3, 3, 1105, -1, 9, 1101, 0, 0,
                    12, 4, 12, 99, 1], [7])[0][-1] == 1

    assert intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                    1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                    999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
                   [7])[0][-1] == 999
    assert intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                    1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                    999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
                   [8])[0][-1] == 1000
    assert intcode([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                    1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                    999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
                   [9])[0][-1] == 1001


def test_day5_part2():
    with open('tests/inputs/05_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert intcode(input_lines, [5])[0][-1] == 10376124


# Day 7
def test_day7_part1_examples():
    assert chain_intercodes([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
                            [4, 3, 2, 1, 0]) == 43210

    assert chain_intercodes(
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23,
         99, 0, 0],
        [0, 1, 2, 3, 4]) == 54321

    assert chain_intercodes(
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
         1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0],
        [1, 0, 4, 3, 2]) == 65210


def test_day7_part1():
    with open('tests/inputs/07_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert chain_intercodes(input_lines, [0, 3, 2, 4, 1]) == 38500


def test_day7_part2_examples():
    assert looping_intcodes(
        [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28,
         1005, 28, 6, 99, 0, 0, 5],
        [9, 8, 7, 6, 5]) == 139629729
    assert looping_intcodes(
        [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
         -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
         53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10],
        [9, 7, 8, 5, 6]) == 18216


def test_day7_part2():
    with open('tests/inputs/07_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert looping_intcodes(input_lines, [7, 5, 9, 6, 8]) == 33660560


# Day 9
def test_day9_part1_examples():
    assert intcode([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99],
                   )[0] == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert len(str(intcode([1102, 34915192, 34915192, 7, 4, 7, 99, 0])[0][-1])) == 16
    assert intcode([104, 1125899906842624, 99])[0][-1] == 1125899906842624


def test_day9_part1():
    with open('tests/inputs/09_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert intcode(input_lines, [1])[0][-1] == 2457252183


def test_day9_part2():
    with open('tests/inputs/09_marcolussetti', 'r') as f:
        file_lines = f.readlines()
    input_lines = [int(line.strip()) for line in file_lines[0].split(",")]
    assert intcode(input_lines, [2])[0][-1] == 70634
