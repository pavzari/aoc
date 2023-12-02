def sum_posssible_game_ids(input):
    sum = 0
    for i in range(len(input)):
        colon_index = input[i].index(":")
        draws = input[i][colon_index + 1 :].split("; ")
        if check_if_valid_game(draws):
            sum += i + 1
    return sum


def check_if_valid_game(draws):
    for draw in draws:
        for cube in draw.split(", "):
            if cube.endswith("red") and int(cube.replace(" red", "")) > 12:
                return False
            elif cube.endswith("green") and int(cube.replace(" green", "")) > 13:
                return False
            elif cube.endswith("blue") and int(cube.replace(" blue", "")) > 14:
                return False
    return True


def sum_of_powers_of_minimum_cubes(input):
    sum = 0
    for i in range(len(input)):
        colon_index = input[i].index(":")
        draws = input[i][colon_index + 1 :].split("; ")
        sum += calculate_power_of_min_cubes(draws)
    return sum


def calculate_power_of_min_cubes(draws):
    max_cubes = {"red": 0, "blue": 0, "green": 0}
    result = 1
    for draw in draws:
        for cube in draw.split(", "):
            if cube.endswith("red"):
                if int(cube.replace(" red", "")) > max_cubes["red"]:
                    max_cubes["red"] = int(cube.replace(" red", ""))
            elif cube.endswith("green"):
                if int(cube.replace(" green", "")) > max_cubes["green"]:
                    max_cubes["green"] = int(cube.replace(" green", ""))
            elif cube.endswith("blue"):
                if int(cube.replace(" blue", "")) > max_cubes["blue"]:
                    max_cubes["blue"] = int(cube.replace(" blue", ""))
    for num in max_cubes.values():
        if num > 0:
            result *= num
    return result


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d2", "r").readlines()]
    print(sum_posssible_game_ids(input))
    print(sum_of_powers_of_minimum_cubes(input))
