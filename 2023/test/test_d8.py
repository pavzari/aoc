from d8 import find_steps, part_two

input = [line.strip() for line in open("input/d8_sample", "r").readlines()]
nodes = {
    input[i].split(" = ")[0]: tuple(input[i].split(" = ")[1][1:9].split(", "))
    for i in range(2, len(input))
}
instructions = [0 if l == "L" else 1 for l in input[0]]

input2 = [line.strip() for line in open("input/d8_sample_2", "r").readlines()]
nodes2 = {
    input2[i].split(" = ")[0]: tuple(input2[i].split(" = ")[1][1:9].split(", "))
    for i in range(2, len(input2))
}
instructions2 = [0 if l == "L" else 1 for l in input2[0]]


def test_d8_a():
    assert find_steps(nodes, instructions) == 6


def test_d8_b():
    assert part_two(nodes2, instructions2) == 6
