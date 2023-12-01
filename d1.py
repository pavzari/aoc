def sum_callibration_values():
    sum = 0
    with open("input/d1", "r") as fp:
        data = [line.strip() for line in fp]
        for value in data:
            value = words_to_digits(value)
            nums = [i for i in [*value] if i.isdigit()]
            if len(nums) == 1:
                sum += int(nums[0] * 2)
            else:
                sum += int(nums[0] + nums[-1])
    return sum


def words_to_digits(string):
    num_strings = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
    }
    for i, n in num_strings.items():
        string = string.replace(i, n)
    return string


print(sum_callibration_values())
