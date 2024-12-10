def part_one(input):
    arr = []
    file_index = 0
    for i, num in enumerate(input):
        if i % 2 != 0:
            arr.extend(["."] * num)
        else:
            arr.extend([file_index] * num)
            file_index += 1

    start = 0
    end = len(arr) - 1

    while start < end:
        while start < end and arr[start] != ".":
            start += 1

        while start < end and isinstance(arr[end], str):
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    return sum([i * num for i, num in enumerate(arr) if isinstance(num, int)])


# def part_two(input):
#     pass


if __name__ == "__main__":
    input = [int(num) for num in open("input/d9_sample", "r").read().strip()]

    print(part_one(input))
    # print(part_two(input))
