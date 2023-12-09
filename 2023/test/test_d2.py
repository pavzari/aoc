from d2 import sum_posssible_game_ids
from d2 import sum_of_powers_of_minimum_cubes

sample_input = [line.strip() for line in open("input/d2_sample", "r").readlines()]


def test_d2_a():
    assert sum_posssible_game_ids(sample_input) == 8


def test_d2_b():
    assert sum_of_powers_of_minimum_cubes(sample_input) == 2286
