from d9 import sum_oasis_values

input = [line.strip() for line in open("input/d9_sample", "r").readlines()]


def test_d9_a():
    assert sum_oasis_values(input) == 114
