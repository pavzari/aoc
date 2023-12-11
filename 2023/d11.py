from pprint import pprint
import itertools


def sum_shortest_paths(input):
    grid = [[pipe for pipe in line] for line in input]
    grid = expand_grid(grid)

    galaxies = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                galaxies.append([x, y])

    unique_galaxy_pairs = list(itertools.combinations(galaxies, 2))

    # find manhattan distance between pairs
    distances = []
    for pair in unique_galaxy_pairs:
        distances.append(sum(abs(val1 - val2) for val1, val2 in zip(pair[0], pair[1])))

    return sum(distances)


def expand_grid(grid):
    # find empty rows
    grid_len = len(grid)
    empty_y = [y for y in range(grid_len) if "#" not in grid[y]]

    for i, y in enumerate(empty_y):
        grid.insert(y + i, ["."] * grid_len)

    # find empty columns
    empty_x = []
    for i in range(len(grid[0])):
        y = [grid[i] for grid in grid]
        if "#" not in y:
            empty_x.append(i)

    for i, x in enumerate(empty_x):
        for row in grid:
            row.insert(x + i, ".")

    return grid


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d11", "r").readlines()]
    print(sum_shortest_paths(input))
