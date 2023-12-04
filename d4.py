def sum_card_points(input):
    total_points = 0
    for card in input:
        all_numbers = card.split(": ")[1].split(" | ")
        card_numbers = [s for s in all_numbers[0].split(" ") if s]
        winning_numbers = [s for s in all_numbers[1].split(" ") if s]
        # print(card_numbers, winning_numbers)

        matches = 0
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1

        card_points = 2 ** (matches - 1) if matches else 0
        total_points += card_points

    return total_points


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d4", "r").readlines()]
    print(sum_card_points(input))
