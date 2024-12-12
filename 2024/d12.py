from collections import deque


def main(some_array):
    directions = (-1, 0), (0, +1), (+1, 0), (0, -1)
    start = 0, 0
    hash = {}

    visited = set()
    for i in range(len(some_array)):
        for y in range(len(some_array)):
            start = i, y
            if start not in visited:
                nodes = find_similar(some_array, directions, start)
                for node in nodes[2]:
                    visited.add(node)
                if nodes[0] not in hash.keys():
                    hash[nodes[0]] = nodes[1] * len(nodes[2])
                else:
                    hash[nodes[0]] += nodes[1] * len(nodes[2])

    print("part_one:", sum(sum for sum in hash.values()))


def find_similar(array, directions, start):
    match = get_item(array, start)
    block = {start}
    visit = deque(block)
    perimeter = 0
    nodes = []
    while visit:
        node = deque.popleft(visit)
        for offset in directions:
            index = get_next(node, offset)
            if not is_valid(array, index):
                perimeter += 1
            elif get_item(array, index) != match:
                perimeter += 1
            elif index not in block:
                block.add(index)
                visit.append(index)
        nodes.append(node)
    return (match, perimeter, nodes)


def get_item(array, index):
    row, column = index
    return array[row][column]


def get_next(node, offset):
    row, column = node
    row_offset, column_offset = offset
    return row + row_offset, column + column_offset


def is_valid(array, index):
    row, column = index
    return 0 <= row < len(array) and 0 <= column < len(array[row])


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d12", "r").readlines()]
    main(input)
