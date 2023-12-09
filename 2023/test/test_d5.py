from d5 import get_lowest_location

sample_input = [
    mapping.split("\n") for mapping in open("input/d5_sample", "r").read().split("\n\n")
]


def test_d5_a():
    assert get_lowest_location(sample_input) == 35
