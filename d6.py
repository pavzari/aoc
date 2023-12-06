def day_six(races):
    result = 1

    for race in races:
        possible_wins = 0
        for i in range(1, race[0] + 1):
            if (race[0] - i) * i > race[1]:
                possible_wins += 1
        result *= possible_wins

    return result


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d6", "r").readlines()]
    times = map(int, input[0].split(": ")[1].split())
    distances = map(int, input[1].split(": ")[1].split())
    races_a = tuple(zip(times, distances))
    print(day_six(races_a))

    time = int("".join(input[0].split(": ")[1].split()))
    distance = int("".join(input[1].split(": ")[1].split()))
    race_b = [(time, distance)]
    print(day_six(race_b))
