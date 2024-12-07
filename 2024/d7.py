from collections import deque
from itertools import product

from timer import timer


def _try_combos(op_hash, target, operands):
    if max(operands) > target:
        return

    # filter out unproductive combos early
    op_combs = op_hash[len(operands) - 1]

    if target % operands[-1] != 0:
        op_combs = [opset for opset in op_combs if opset[-1] != "*"]

    if str(target)[-len(str(operands[-1])) :] != str(operands[-1]):
        op_combs = [opset for opset in op_combs if opset[-1] != "||"]

    if str(target)[0 : len(str(operands[-1]))] != str(operands[-1]):
        op_combs = [opset for opset in op_combs if opset[0] != "||"]

    if target % 2 != 0 and operands[-1] % 2 == 0:
        op_combs = [opset for opset in op_combs if opset[-1] != "+"]

    for opset in op_combs:
        d_operands = deque(operands)
        skip_opset = False
        for op in opset:
            a, b = d_operands.popleft(), d_operands.popleft()
            if op == "+":
                res = a + b
            elif op == "*":
                res = a * b
            elif op == "||":
                res = int(str(a) + str(b))
            if res > target:
                skip_opset = True
                break
            d_operands.appendleft(res)
        if skip_opset:
            continue
        if d_operands[0] == target:
            return True


def part_one(input):
    # precompute operator combinations
    operators_needed = {len(eq[1]) - 1 for eq in input}
    op_hash = {num: list(product(["+", "*"], repeat=num)) for num in operators_needed}

    return sum(
        equation[0]
        for equation in input
        if _try_combos(op_hash, equation[0], equation[1])
    )


def part_two(input):
    # precompute operator combinations
    operators_needed = {len(eq[1]) - 1 for eq in input}
    op_hash = {
        num: list(product(["+", "*", "||"], repeat=num)) for num in operators_needed
    }

    return sum(
        equation[0]
        for equation in input
        if _try_combos(op_hash, equation[0], equation[1])
    )


if __name__ == "__main__":
    input = [line.strip().split(" ") for line in open("input/d7", "r").readlines()]
    input = [
        (int(equation[0][:-1]), list(map(int, equation[1:]))) for equation in input
    ]

    with timer("part_1") as t:
        print("part_1:", part_one(input))

    with timer("part_2") as t:
        print("part_2:", part_two(input))
