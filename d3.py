import re


def sum_engine_part_numbers(input):
    # padding the input with "." to avoid dealing with 'edge' cases
    input = ["." + row + "." for row in input]
    row_len = len(input[0])
    input.insert(0, "." * row_len)
    input.insert(len(input), "." * row_len)

    symbols = ["@", "/", "#", "$", "&", "%", "-", "*", "+", "="]
    sum = 0

    for line in range(len(input)):
        for num_match in re.finditer(r"\d{1,3}", input[line]):
            number = input[line][num_match.start() : num_match.end()]
            start_index = num_match.start()
            end_index = num_match.end() - 1

            possible_symbols = []

            # same line
            possible_symbols.append(input[line][start_index - 1])
            possible_symbols.append(input[line][end_index + 1])

            # line above
            possible_symbols.append(input[line - 1][start_index - 1 : end_index + 2])

            # line bellow
            possible_symbols.append(input[line + 1][start_index - 1 : end_index + 2])

            for symbol in symbols:
                if symbol in "".join(possible_symbols):
                    sum += int(number)
                    break

    return sum


def sum_engine_gear_ratios():
    """Istead of searching for all symbols around a number, look for a star and note it's position:
    create a dict with a list of numbers and coordinates of stars that the number is adjacent to
    then check which two numbers share the same star.
    """
    pass


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d3", "r").readlines()]
    print(sum_engine_part_numbers(input))

# Input symbols: {'@', '/', '#', '$', '&', '%', '-', '*', '+', '='}

# symbols = []
# for x in input:
#     for n in x:
#         if not n.isdigit() and n != ".":
#             symbols.append(n)
# print(set(symbols))
