import re

X_LEN = 101 - 1
Y_LEN = 103 - 1
TIME = 100


def _safety_factor(positions):
    # quadrants
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for pos in positions:
        if (0 <= pos[0] < (X_LEN / 2)) and (0 <= pos[1] < (Y_LEN / 2)):
            q1 += 1
        if ((X_LEN / 2) < pos[0] <= X_LEN) and (0 <= pos[1] < (Y_LEN / 2)):
            q2 += 1
        if (0 <= pos[0] < (X_LEN / 2)) and ((Y_LEN / 2) < pos[1] <= Y_LEN):
            q3 += 1
        if ((X_LEN / 2) < pos[0] <= X_LEN) and ((Y_LEN / 2) < pos[1] <= Y_LEN):
            q4 += 1

    return q1 * q2 * q3 * q4


def _get_new_position(current_pos, velocity):
    new_x = current_pos[0] + velocity[0]
    new_y = current_pos[1] + velocity[1]

    if new_x > X_LEN:
        new_x = (current_pos[0] + velocity[0]) - X_LEN - 1

    if new_x < 0:
        new_x = X_LEN + (current_pos[0] + velocity[0]) + 1

    if new_y > Y_LEN:
        new_y = (current_pos[1] + velocity[1]) - Y_LEN - 1

    if new_y < 0:
        new_y = Y_LEN + (current_pos[1] + velocity[1]) + 1

    return (new_x, new_y)


def _print_grid(positions):
    grid = [["." for _ in range(X_LEN)] for _ in range(Y_LEN)]

    for x, y in positions:
        if 0 <= x < X_LEN and 0 <= y < Y_LEN:
            grid[y][x] = "X"

    for row in grid:
        print(" ".join(row))


def part_one(input):
    final_positions = []

    for robot in input:
        current_pos = robot[0]
        velocity = robot[1]
        for _ in range(TIME):
            current_pos = _get_new_position(current_pos, velocity)
        final_positions.append(current_pos)

    return _safety_factor(final_positions)


def part_two(input):
    iterations = []
    safety_factors = []
    start = input

    for i in range(10000):
        positions = []
        new_start = []
        for robot in start:
            current_pos = robot[0]
            velocity = robot[1]
            next_position = _get_new_position(current_pos, velocity)
            positions.append(next_position)
            new_start.append([next_position, velocity])

        iterations.append(i)
        safety_factor = _safety_factor(positions)
        safety_factors.append(safety_factor)
        start = new_start

        if safety_factor < 100000000:
            # starting at 0 so answer is i + 1!
            print("________SECONDS_ELAPSED_______:", i + 1)
            _print_grid(positions)

    # looking at the iterations with lowest safety factors:

    # plt.plot(iterations, safety_factors, marker='o')
    # plt.xlabel('Iteration Step')
    # plt.ylabel('Safety factor')
    # plt.title('Iteration vs Safety factor')
    # plt.grid(True)
    # plt.show()

    # print([(i, val) for i, val in enumerate(safety_factors) if val < 100000000])


if __name__ == "__main__":

    def _parse_input(robot) -> list[tuple]:
        # [start (x, y), velocity (x, y)]
        start_pos = re.findall(r"\d+", robot[0])
        velocity = re.findall(r"-?\d+", robot[1])
        return [
            (int(start_pos[0]), int(start_pos[1])),
            (int(velocity[0]), int(velocity[1])),
        ]

    input = [
        _parse_input(robot.strip().split(" "))
        for robot in open("input/d14", "r").readlines()
    ]

    print(len(input))

    print("part_one:", part_one(input))
    print("part_two:", part_two(input))
