MOVE_DIR = {
    ">": lambda current: (current[0] + 1, current[1]),
    "<": lambda current: (current[0] - 1, current[1]),
    "v": lambda current: (current[0], current[1] + 1),
    "^": lambda current: (current[0], current[1] - 1),
}

CHANGE_DIR = {"v": "<", "<": "^", "^": ">", ">": "v"}


def part_one(grid, len_x, len_y):
    visited = []
    start = [key for key, value in grid.items() if value in MOVE_DIR.keys()][0]
    current_coord = start
    direction = grid[current_coord]

    while True:
        next_coord = MOVE_DIR[direction](current_coord)

        # check for boundaries
        if not (0 <= next_coord[0] < len_x and 0 <= next_coord[1] < len_y):
            visited.append(current_coord)
            break

        elif grid[next_coord] == "#":
            direction = CHANGE_DIR[direction]

        else:
            visited.append(current_coord)
            current_coord = next_coord
            direction = direction

    return visited


def part_two(grid, len_x, len_y, visited):
    loops = 0
    start = [key for key, value in grid.items() if value in MOVE_DIR.keys()][0]
    visited.remove(start)

    for coord in visited:
        new_grid = dict(grid)
        new_grid[coord] = "#"

        # use a set over a list to speed things up!!
        # tuple ((x, y,), direction)
        visited = set()
        current_coord = start
        direction = new_grid[current_coord]

        while True:
            next_coord = MOVE_DIR[direction](current_coord)

            # check for boundaries
            if not (0 <= next_coord[0] < len_x and 0 <= next_coord[1] < len_y):
                break

            elif new_grid[next_coord] == "#":
                direction = CHANGE_DIR[direction]

            else:
                # check if the coord with the same direction has already been visited to
                # detect looping
                if (current_coord, direction) in visited:
                    loops += 1
                    break
                visited.add((current_coord, direction))
                current_coord = next_coord
                direction = direction
    return loops


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d6", "r").readlines()]
    # (x,y) grid with (0, 0) point in the top left.
    grid = {(x, y): val for y, line in enumerate(input) for x, val in enumerate(line)}

    # place obstacles on the path visited in part_one instead of brute-forcing all posible location
    visited = part_one(grid, len(input[0]), len(input))
    print("part_1:", len(set(visited)))
    print("part_2:", part_two(grid, len(input[0]), len(input), set(visited)))
