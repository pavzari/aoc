from collections import Counter


def part_one(left_list, right_list):
    answer = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        answer += abs(left - right)
    return answer


def part_two(left_list, right_list):
    right_count = dict(Counter(right_list))
    return sum([num * right_count.get(num, 0) for num in left_list])


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d1", "r").readlines()]
    left_list = []
    right_list = []

    for line in input:
        split = line.split("   ")
        left_list.append(int(split[0]))
        right_list.append(int(split[1]))

    print(part_one(left_list, right_list))
    print(part_two(left_list, right_list))
