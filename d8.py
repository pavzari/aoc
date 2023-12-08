def find_steps(input):
    nodes = {
        input[i].split(" = ")[0]: tuple(input[i].split(" = ")[1][1:9].split(", "))
        for i in range(2, len(input))
    }

    instructions = [0 if l == "L" else 1 for l in input[0]]

    next_node = "AAA"
    steps_taken = 0
    resume = True
    while resume:
        for step in instructions:
            steps_taken += 1
            if nodes[next_node][step] == "ZZZ":
                resume = False
                break
            next_node = nodes[next_node][step]

    return steps_taken


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d8", "r").readlines()]
    print(find_steps(input))
