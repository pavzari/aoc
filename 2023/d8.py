import math


def find_steps(nodes, instructions):
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


def part_two(nodes, instructions):
    starting_nodes = [node for node in nodes.keys() if node[2] == "A"]

    # next_nodes = starting_nodes
    # steps_taken = 0
    # resume = True
    # while resume:
    #     for step in instructions:
    #         steps_taken += 1
    #         new_nodes = []
    #         for node in next_nodes:
    #             new_nodes.append(nodes[node][step])

    #         if all(node[2] == "Z" for node in new_nodes):
    #             resume = False
    #             break

    #         next_nodes = new_nodes

    # return steps_taken

    steps_to_z = []
    for node in starting_nodes:
        next_node = node
        steps_taken = 0
        resume = True
        while resume:
            for step in instructions:
                steps_taken += 1
                if nodes[next_node][step][2] == "Z":
                    resume = False
                    break
                next_node = nodes[next_node][step]

        steps_to_z.append(steps_taken)

    return math.lcm(*steps_to_z)


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d8", "r").readlines()]
    nodes = {
        input[i].split(" = ")[0]: tuple(input[i].split(" = ")[1][1:9].split(", "))
        for i in range(2, len(input))
    }

    instructions = [0 if l == "L" else 1 for l in input[0]]
    print(find_steps(nodes, instructions))
    print(part_two(nodes, instructions))
