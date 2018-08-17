"""# import collections"""

def card_value_hand(hand):
    '''calculates card values'''
    exception_case = [2, 3, 4, 5, 14]
    card_value = ['--23456789TJQKA'.index(c) for c, s in hand]
    if card_value == exception_case:
        card_value.remove(14)
        card_value.add(1)
    card_value = sorted(card_value, reverse=True)
    return card_value

def is_straight(hand):
    ''' Straight function '''
    return len(card_value_hand(hand)) == 5 and (max(card_value_hand(
        hand))-min(card_value_hand(hand)) == 4)

def is_flush(hand):
    ''' flush function '''
    return len(set(s for c, s in hand)) == 1

def kind(hand, n_len):
    ''' To determine the kind of the function'''
    for ranks in card_value_hand(hand):
        if card_value_hand(hand).count(ranks) == n_len:
            return ranks
    return None

# def is_four_of_a_kind(hand):
#     ''' Four of a kind hand function '''
#     return list(collections.Counter(card_value_hand(hand)).values()) == [4, 1]

# def is_fullhouse(hand):
#     ''' Full House hand function '''
#     return sorted(list(collections.Counter(card_value_hand(hand)).values())) == [2, 3]

# def is_three_of_kind(hand):
#     ''' Three of kind hand function '''
#     bool_val = sorted(list(collections.Counter(card_value_hand(hand)).values())) == [1, 1, 3]
#     return bool_val

# def is_twopair(hand):
#     ''' Two pair hand function '''
#     bool_val = sorted(list(collections.Counter(card_value_hand(hand)).values())) == [1, 2, 2]
#     return bool_val

# def is_onepair(hand):
#     ''' One pair hand function '''
#     bool_val = sorted(list(collections.Counter(card_value_hand(hand)).values())) == [1, 1, 1, 2]
#     return bool_val

def hand_rank(hand):
    ''' ranks the card '''
    hand_ranks = card_value_hand(hand)
    rank = (0, hand_ranks)
    if is_flush(hand) and is_straight(hand):
        rank = (8,)

    elif kind(hand, 4):
        rank = (7,)

    elif kind(hand, 3) and kind(hand, 2):
        rank = (6, )

    elif is_flush(hand):
        rank = (5, hand_ranks)

    elif is_straight(hand):
        rank = (4, hand_ranks)

    elif kind(hand, 3):
        return (3, kind(hand, 2), hand_ranks)

    elif kind(hand, 2) and kind(sorted(hand, reverse=True), 2) and kind(\
    hand, 2) != kind(sorted(hand, reverse=True), 2):
        return (2, kind(hand, 2), kind(sorted(hand, reverse=True), 2))

    elif kind(hand, 2):
        return (1, kind(hand, 2))
    return rank

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
