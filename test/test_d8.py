from d8 import find_steps

input = [line.strip() for line in open("input/d8_sample", "r").readlines()]


def test_d8_a():
    assert find_steps(input) == 6
