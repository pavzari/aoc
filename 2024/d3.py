import re


def part_one(input):
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    return sum([int(match[0]) * int(match[1]) for match in matches])


def part_two(input):
    match = re.search(r"don't\(\)(?:(?!do\(\)).)*do\(\)", input)
    if match:
        part_two(input[: match.start()] + input[match.end() :])
    else:
        # remove last don't() -> end of input if present
        if match := re.search(r"don't", input):
            print(part_one(input[: match.start()]))
        else:
            print(part_one(input))


if __name__ == "__main__":
    input = open("input/d3", "r").read().replace("\n", "")

    print(part_one(input))
    part_two(input)
