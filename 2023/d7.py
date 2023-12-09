from functools import cmp_to_key


def total_winnings(input):
    hands = []
    for line in input:
        hand, bid = line.split(" ")
        hand_dict = {card: hand.count(card) for card in hand}
        hand_dict = dict(sorted(hand_dict.items(), key=lambda x: -x[1]))
        hand_rank_str = "".join(map(str, hand_dict.values()))
        hands.append((hand_rank_str, hand, bid))

    # print(hands)
    hand_compare_key = cmp_to_key(compare_hands)
    sorted_hands = sorted(hands, key=hand_compare_key, reverse=True)
    # print(sorted_hands)

    sum = 0
    for i, hand in enumerate(sorted_hands):
        sum += (i + 1) * int(hand[2])

    return sum


def compare_hands(hand_a, hand_b):
    """
    Hand sorting function: receives a tuple where first item is a string
    representation of a number of unique cards and their count in a hand.
    This is then used to assign a rank to both hands that are being compared.
    If the ranks are the same, individual cards are then compared one by one
    until a stronger card is found in order to break the tie.
    """
    cards = "AKQJT98765432"
    rank_map = {
        "5": 7,
        "41": 6,
        "32": 5,
        "311": 4,
        "221": 3,
        "2111": 2,
        "11111": 1,
    }

    # print("comparing:", hand_a, hand_b)
    hand_rank1, hand1, bid1 = hand_a
    hand_rank2, hand2, bid2 = hand_b

    if rank_map[hand_rank1] == rank_map[hand_rank2]:
        for i in range(5):
            if cards.index(hand1[i]) != cards.index(hand2[i]):
                if cards.index(hand1[i]) > cards.index(hand2[i]):
                    return 1
                else:
                    return -1
    if rank_map[hand_rank1] < rank_map[hand_rank2]:
        return 1
    else:
        return -1


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d7", "r").readlines()]
    print(total_winnings(input))

"""
    1. 5 same (KKKKK)
    2. 4 same, 1 same (KKKK3)
    3. 3 same, 2 same
    4. 3 same, 1 same, 1 same
    5. 2 same, 2 same, 1 same
    6. 2 same, 1 same, 1 same, 1 same
    7. 1 same, 1 same, 1 same, 1 same, 1 same
"""
