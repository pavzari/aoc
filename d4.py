def sum_card_points(input):
    total_points = 0
    initial_matches = {}
    for card in input:
        card_number = [num for num in card.split(": ")[0].split(" ") if num][1]
        all_numbers = card.split(": ")[1].split(" | ")
        card_numbers = [s for s in all_numbers[0].split(" ") if s]
        winning_numbers = [s for s in all_numbers[1].split(" ") if s]

        matches = 0
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1

        card_points = 2 ** (matches - 1) if matches else 0
        total_points += card_points

        initial_matches[int(card_number)] = matches

    return total_points, initial_matches


def total_cards_won(initial_matches):
    total_seen = {card: 1 for card in range(1, len(initial_matches) + 1)}

    for card in total_seen.keys():
        if initial_matches[card] > 0:
            for _ in range(total_seen[card]):
                for i in range(card + 1, card + initial_matches[card] + 1):
                    total_seen[i] += 1

    return sum(total_seen.values())


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d4", "r").readlines()]
    print(sum_card_points(input)[0])
    print(total_cards_won(sum_card_points(input)[1]))
