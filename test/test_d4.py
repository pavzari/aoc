from d4 import sum_card_points

sample_input = [line.strip() for line in open("input/d4_sample", "r").readlines()]


def test_d4_a():
    assert sum_card_points(sample_input) == 13
