def part_one(input):
    coords = []
    for line in range(len(input)):
        for index, letter in enumerate(input[line]):
            if letter == "X":
                # diagonal
                ne = [(input[line - i][index + i]) for i in range(0, 4)]
                se = [(input[line + i][index + i]) for i in range(0, 4)]
                sw = [(input[line + i][index - i]) for i in range(0, 4)]
                nw = [(input[line - i][index - i]) for i in range(0, 4)]

                if "".join(ne) == "XMAS":
                    coords.append((line, index, line - 3, index + 3))
                if "".join(se) == "XMAS":
                    coords.append((line, index, line + 3, index + 3))
                if "".join(sw) == "XMAS":
                    coords.append((line, index, line + 3, index - 3))
                if "".join(nw) == "XMAS":
                    coords.append((line, index, line - 3, index - 3))

                # vertical
                up = [(input[line - i][index]) for i in range(0, 4)]
                down = [(input[line + i][index]) for i in range(0, 4)]

                if "".join(up) == "XMAS":
                    coords.append((line, index, line - 3, index))
                if "".join(down) == "XMAS":
                    coords.append((line, index, line + 3, index))

                # horizontal
                if input[line][index : index + 4] == "XMAS":
                    coords.append((line, index, line, index + 3))
                if input[line][index - 3 : index + 1][::-1] == "XMAS":
                    coords.append((line, index, line, index - 3))

    return len(coords)


def part_two(input):
    count = 0
    for line in range(len(input)):
        for index, letter in enumerate(input[line]):
            if letter == "A":
                ne = input[line - 1][index + 1]
                se = input[line + 1][index + 1]
                sw = input[line + 1][index - 1]
                nw = input[line - 1][index - 1]

                if (ne + "A" + sw == "MAS" or ne + "A" + sw == "SAM") and (
                    nw + "A" + se == "SAM" or nw + "A" + se == "MAS"
                ):
                    count += 1
    return count


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d4", "r").readlines()]

    # padding the input with 4 x "." to avoid dealing with 'edge' cases
    row_len = len(input[0])
    input = ["...." + row + "...." for row in input]
    for i in reversed(range(3)):
        dots = ".." * (2 * (4 - i))
        input.insert(0, ".." * row_len + dots)
        input.append(".." * row_len + dots)

    print(part_one(input))
    print(part_two(input))
