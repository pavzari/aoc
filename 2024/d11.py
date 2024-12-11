from collections import Counter


def part_one(input):
    BLINK = 25
    input = input
    for _ in range(BLINK):
        nums = []
        for num in input:
            if num == "0":
                nums.append("1")
            elif len(num) % 2 == 0:
                a, b = num[: (len(num) // 2)], num[len(num) // 2 :]
                nums.append(a)
                # remove leading 0's from b
                nums.append(str(int(b)))
            else:
                nums.append(str(int(num) * 2024))
        input = nums
    return len(input)


def _hash_insert(item, count, hash):
    if item not in hash.keys():
        hash[item] = count
    else:
        hash[item] += count


def part_two(input):
    BLINK = 75
    input = dict(Counter(input))

    for _ in range(BLINK):
        hash = {}
        for num, count in input.items():
            if num == "0":
                _hash_insert("1", count, hash)
            elif len(num) % 2 == 0:
                a, b = num[: (len(num) // 2)], num[len(num) // 2 :]
                _hash_insert(a, count, hash)
                _hash_insert(str(int(b)), count, hash)
            else:
                _hash_insert(str(int(num) * 2024), count, hash)
        input = hash
    return sum([count for count in hash.values()])


if __name__ == "__main__":
    input = [num for num in open("input/d11", "r").read().strip().split(" ")]

    print(part_one(input))
    print(part_two(input))
