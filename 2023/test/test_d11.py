from d11 import sum_shortest_paths

input = [line.strip() for line in open("input/d11_sample", "r").readlines()]


def test_d9_a():
    assert sum_shortest_paths(input) == 374
