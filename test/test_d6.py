from d6 import day_six

input = [line.strip() for line in open("input/d6_sample", "r").readlines()]
times = map(int, input[0].split(": ")[1].split())
distances = map(int, input[1].split(": ")[1].split())
races = tuple(zip(times, distances))


def test_d4_a():
    assert day_six(races) == 288
