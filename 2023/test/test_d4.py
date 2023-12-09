from d4 import sum_card_points, total_cards_won

sample_input = [line.strip() for line in open("input/d4_sample", "r").readlines()]


def test_d4_a():
    assert sum_card_points(sample_input)[0] == 13


def test_d4_b():
    assert total_cards_won(sum_card_points(sample_input)[1]) == 30
