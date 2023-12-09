from d3 import sum_engine_part_numbers

sample_input = [line.strip() for line in open("input/d3_sample", "r").readlines()]


def test_d3_a():
    assert sum_engine_part_numbers(sample_input) == 4361
