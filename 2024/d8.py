from itertools import combinations


def _find_harmonics(a, b, bounds):
    nodes = [a, b]

    diff = (a[0] - b[0], a[1] - b[1])
    anti = (a[0] + diff[0], a[1] + diff[1])

    while (0 <= anti[0] < bounds[0]) and (0 <= anti[1] < bounds[1]):
        nodes.append(anti)
        anti = (anti[0] + diff[0], anti[1] + diff[1])

    return nodes


def _find_antinode_coords(a, b):
    diff = (a[0] - b[0], a[1] - b[1])
    return (a[0] + diff[0], a[1] + diff[1])


def _in_grid(coord, bounds):
    return (0 <= coord[0] < bounds[0]) and (0 <= coord[1] < bounds[1])


def part_one_two(input, bounds):
    unique_antinodes = set()
    unique_harmonics = set()

    for coords in input.values():
        combos = list(combinations(coords, 2))
        for combo in combos:
            a_anti = _find_antinode_coords(combo[1], combo[0])
            b_anti = _find_antinode_coords(combo[0], combo[1])

            if _in_grid(a_anti, bounds):
                unique_antinodes.add(a_anti)

            if _in_grid(b_anti, bounds):
                unique_antinodes.add(b_anti)

            unique_harmonics.update(_find_harmonics(combo[1], combo[0], bounds))
            unique_harmonics.update(_find_harmonics(combo[0], combo[1], bounds))

    return len(unique_antinodes), len(unique_harmonics)


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d8", "r").readlines()]
    grid_bounds = (len(input[0]), len(input))

    grid = {
        (x, y): val
        for y, line in enumerate(input)
        for x, val in enumerate(line)
        if val != "."
    }

    # coords for each antenna type
    antennas = {}
    for key, value in grid.items():
        if value not in antennas:
            antennas[value] = [key]
        else:
            antennas[value].append(key)

    print(part_one_two(antennas, grid_bounds))
