cimport re


def _calc_presses(input: list[list[tuple]]) -> list[tuple]:
    # each button <= 100 presses
    # returns (a, b) button presses
    button_range = (1, 101)
    solutions = []
    ba_x, ba_y = input[0]
    bb_x, bb_y = input[1]
    tx, ty = input[2]

    for a in range(*button_range):
        for b in range(*button_range):
            if (ba_x * a + bb_x * b == tx) and (ba_y * a + bb_y * b == ty):
                solutions.append((a, b))
    return solutions


def _calc_presses_part_two(input: list[list[tuple]]) -> tuple:
    ba_x, ba_y = input[0]
    bb_x, bb_y = input[1]
    tx, ty = input[2]
    tx = tx + 10000000000000
    ty = ty + 10000000000000

    b = ((ba_x * ty) - (tx * ba_y)) / ((ba_x * bb_y) - (bb_x * ba_y))
    a = (ty - (bb_y * b)) / ba_y

    if a.is_integer() and b.is_integer():
        return (a, b)


def part_one(input):
    # tokens: a:3, b:1
    winning_combs = [
        _calc_presses(machine) for machine in input if _calc_presses(machine)
    ]
    return sum([(press[0][0] * 3) + (press[0][1] * 1) for press in winning_combs])


def part_two(input):
    winning_combs = [
        _calc_presses_part_two(machine)
        for machine in input
        if _calc_presses_part_two(machine)
    ]
    return int(sum([(press[0] * 3) + (press[1] * 1) for press in winning_combs]))


if __name__ == "__main__":

    def _parse_input(machine) -> list[tuple]:
        # (x, y) x 3
        button_a = re.findall(r"\d+", machine[0])
        button_b = re.findall(r"\d+", machine[1])
        prize_location = re.findall(r"\d+", machine[2])
        return [
            (int(button_a[0]), int(button_a[1])),
            (int(button_b[0]), int(button_b[1])),
            (int(prize_location[0]), int(prize_location[1])),
        ]

    input = [
        _parse_input(machine.split("\n"))
        for machine in open("input/d12", "r").read().split("\n\n")
    ]

    print("part_one:", part_one(input))
    print("part_two:", part_two(input))
