def sum_oasis_values(input):
    """
    last: last digits of all list that are the result
    of differences between elements of previous lists
    starting with the initial sequence.

    new_last: all the numbers that each of the sub sequences.
    The last value is the next value for the original sequence.
    """
    result = []
    for line in input:
        seq = list(map(int, line.split(" ")))
        last = [seq[-1]]
        while len(set(seq)) > 1:
            seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
            last.append(seq[-1])

        last = sorted(last)
        new_last = []
        new_last.append(last[0])

        for i in range(1, len(last)):
            new_last.append(new_last[-1] + last[i])

        result.append(new_last[-1])

    return sum(result)


def extrapolate_backwards(input):
    result = []
    for line in input:
        seq = list(map(int, line.split(" ")))
        first = [seq[0]]
        while len(set(seq)) > 1:
            seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
            first.append(seq[0])

        new_first = []
        new_first.append(first[-1])

        for i in range(len(first) - 2, -1, -1):
            new_first.append(first[i] - new_first[-1])

        result.append(new_first[-1])

    return sum(result)


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d9", "r").readlines()]
    print(sum_oasis_values(input))
    print(extrapolate_backwards(input))
