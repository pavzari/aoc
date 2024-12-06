def _check_update(update: list, rules_hash: dict):
    for index, page in enumerate(update):
        if index == 0:
            after = update[1:]
            for pg in after:
                if pg not in rules_hash[page]:
                    return False
        elif index == (len(update) - 1):
            before = update[:index]
            for pg in before:
                if pg not in rules_hash:
                    if pg in rules_hash[update[index]]:
                        return False
                    else:
                        continue
                else:
                    if update[index] not in rules_hash[pg]:
                        return False
        else:
            after = update[index + 1 :]
            before = update[:index]
            for pg in after:
                if page not in rules_hash:
                    continue
                else:
                    if pg not in rules_hash[page]:
                        return False

            for pg in before:
                if pg not in rules_hash:
                    continue
                else:
                    if update[index] not in rules_hash[pg]:
                        return False
    return True


def part_one(rules_hash, updates):
    correct = [update for update in updates if _check_update(update, rules_hash)]
    return sum([list(map(int, cor))[len(cor) // 2] for cor in correct])


# def part_two(rules_hash, updates):
#     pass


if __name__ == "__main__":
    rules, updates = open("input/d5", "r").read().split("\n\n")
    updates = [update.split(",") for update in updates.strip().split("\n")]
    rules = [rule.split("|") for rule in rules.strip().split("\n")]

    rules_hash = {}
    for rule in rules:
        if rule[0] not in rules_hash:
            rules_hash[rule[0]] = [rule[1]]
        else:
            rules_hash[rule[0]].append(rule[1])

    # print(rules_hash)
    # print(updates)

    print(part_one(rules_hash, updates))
    # print(part_two(rules_hash, updates))
