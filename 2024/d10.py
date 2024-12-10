def _next_moves(coord, cur_value, grid, bounds):
    next_valid_moves = []
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for move in moves:
        x = coord[0] + move[0]
        y = coord[1] + move[1]
        # check for bounds and only select the coord with current + 1 value
        if ((0 <= x < bounds[0]) and (0 <= y < bounds[1])) and (
            grid[(x, y)] == str(int(cur_value) + 1)
        ):
            next_valid_moves.append((x, y))
    return next_valid_moves


def part_one_two(grid, trailheads, bounds):
    trails = {}

    def recurse_paths(coord, cur_value, grid, bounds):
        if cur_value == 9:
            return [[coord]]
        paths = []
        for move in _next_moves(coord, cur_value, grid, bounds):
            for path in recurse_paths(move, cur_value + 1, grid, bounds):
                paths.append([coord] + path)
        return paths

    for start, head in trailheads.items():
        trails[start] = recurse_paths(start, int(head), grid, bounds)

    # if there are multiple paths to the same dest, remove them and keep one
    no_dup_dest = {
        head: {trail[-1] for trail in value} for head, value in trails.items()
    }
    print("part_1:", sum([len(paths) for paths in no_dup_dest.values()]))
    print("part_2:", sum([len(paths) for paths in trails.values()]))


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d10", "r").readlines()]
    grid_bounds = (len(input[0]), len(input))

    grid = {(x, y): val for y, line in enumerate(input) for x, val in enumerate(line)}
    trailheads = {coord: num for coord, num in grid.items() if num == "0"}

    # print(grid)
    # print(trailheads)

    print(part_one_two(grid, trailheads, grid_bounds))
