def day_ten_maze(input):
    maze = [[pipe for pipe in line] for line in input]

    # maze x and y len
    grid_x = len(maze)
    grid_y = len(maze[0])

    directions = {
        "N": [-1, 0],
        "E": [0, 1],
        "S": [1, 0],
        "W": [0, -1],
    }

    pipes = {
        "|": ["N", "S"],
        "-": ["E", "W"],
        "L": ["N", "E"],
        "J": ["N", "W"],
        "7": ["S", "W"],
        "F": ["S", "E"],
    }

    # find starting position coordinates and pipe
    starting_position = None

    for x in range(grid_x):
        for y in range(grid_y):
            if maze[y][x] == "S":
                starting_position = [y, x]

    starting_possible_directions = []
    for direction, coord in directions.items():
        if (
            maze[starting_position[0] + coord[0]][starting_position[1] + coord[1]]
            != "."
        ):
            starting_possible_directions.append(direction)

    starting_pipe = None

    for pipe, dirs in pipes.items():
        a, b = starting_possible_directions
        if a in dirs and b in dirs:
            starting_pipe = pipe

    print("Starting position coords and pipe:", starting_position, starting_pipe)

    # walk the maze

    # current_position = starting_position
    # current_pipe = starting_pipe
    # resume = True

    # path = []
    # while resume:
    #     direction = pipes[current_pipe][1]

    #     coord = directions[direction]
    #     if [current_position[0] + coord[0], current_position[1] + coord[1]] == [1, 1]:
    #         resume = False
    #         break

    #     next_pipe = maze[current_position[0] + coord[0]][current_position[1] + coord[1]]
    #     current_pipe = next_pipe
    #     current_position = [
    #         current_position[0] + coord[0],
    #         current_position[1] + coord[1],
    #     ]
    #     path.append((next_pipe, current_position))

    # print(path)


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d10_sample", "r").readlines()]
    print(day_ten_maze(input))
