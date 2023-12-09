from d7 import total_winnings

input = [line.strip() for line in open("input/d7_sample", "r").readlines()]


def test_d7_a():
    assert total_winnings(input) == 6440
