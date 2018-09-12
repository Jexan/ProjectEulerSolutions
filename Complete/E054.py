# How many times Player 1 wins in the hands displayed in p054_poker.txt
# OPTIMAL (<0.4s)
#
# APPROACH:
#     Brute force approach. The challenge is the 
#     complexity, not the amount of calculations.

from collections import Counter
import os

FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'p054_poker.txt')

def_vals = {'T':10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
def_vals.update({str(i): i for i in range(2, 10)})

class Card:
    def __init__(self, moniker):
        self.val = def_vals[moniker[0]]
        self.suit = moniker[1]
        self.moniker = moniker

    def __or__(self, other):
        return self.suit == other.suit

    def __hash__(self):
        return hash(self.moniker)

    def __repr__(self):
        return self.moniker

def parse_hand(cards):
    return tuple(Card(card) for card in cards)

def parse_hands(hands):
    elements = hands.split(' ')
    return parse_hand(elements[:5]), parse_hand(elements[5:])

def max_beats_out(l1, l2):
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            continue

        return l1[i] > l2[i]

def does_p1_win(p1, p2):
    info_1, info_2 = check_rank(p1), check_rank(p2)

    if info_1[0] > info_2[0]:
        return True
    elif info_1[0] == info_2[0]:
        if info_1[1] is None:
            return max_beats_out(info_1[2], info_2[2])
        elif isinstance(info_1[1], tuple):
            max_1, max_2 = max(info_1[1]), max(info_2[1])
            min_1, min_2 = min(info_1[1]), min(info_2[1])
            left_1, left_2 = info_1[2][0], info_1[2][1]

            if max_1 > max_2:
                return True
            elif max_1 == max_2:
                return min_1 > min_2 or (min_2 == min_1 and left_1 > left_2)
        else:
            if info_1[1] == info_2[1]:
                return max_beats_out(info_1[2], info_2[2])
            else:
                return info_1[1] > info_2[1]

        return result
    
    return False 

def check_rank(p):
    royal_flush = set((10, 11, 12, 13, 14))
    can_do_royal_flush = True
    max_so_far = 0

    for card in p:
        val = card.val

        if max_so_far < val: max_so_far = val

        if can_do_royal_flush and val in royal_flush:
            royal_flush.remove(val)
        else:
            can_do_royal_flush = False

    numbers = Counter(card.val for card in p)
    times = numbers.values()
    key_times = numbers.items()
    
    two_vals = tuple(val for val, times in key_times if times == 2)
    three_vals = tuple(val for val, times in key_times if times == 3)
    four_vals = tuple(val for val, times in key_times if times == 4)
    sorted_vals = sorted(numbers.keys())
    cards_same_suit = same_suit(p)
    consecutive = consecutive_vals(sorted_vals)

    if 14 in numbers and consecutive and cards_same_suit:
        rank = (10, None)
    elif consecutive and cards_same_suit:
        rank = (9, None)
    elif four_vals:
        rank = (8, four_vals[0])
    elif three_vals and two_vals:
        rank = (7, three_vals[0])
    elif cards_same_suit:
        rank = (6, None)
    elif consecutive:
        rank = (5, None)
    elif three_vals:
        rank = (4, three_vals[0]) 
    elif two_vals:
        if len(two_vals) == 2:
            rank = (3, two_vals)
        else:
            rank = (2, two_vals[0])
    else:
        rank = (1, max_so_far)

    if rank[1] is not None:
        val = rank[1]

        if isinstance(val, tuple):
            sorted_vals = list(i for i in sorted_vals if i not in val)
        else:
            sorted_vals = list(i for i in sorted_vals if i != val)
            
    return (*rank, sorted_vals[::-1])

def same_suit(hand):
    prev = hand[0]
    for card in hand[1:]:
        if not (card | prev):
            return False

    return True

def consecutive_vals(iterator):
    if len(iterator) != 5:
        return False
    prev = iterator[0]
    for n in iterator[1:]:
        if n - prev != 1:
            return False

        prev = n

    return True 

def get_result(cards):
    return len(list(i for i in (does_p1_win(*parse_hands(hands)) for hands in cards.splitlines()) if i))

with open(FILE_DIR, 'r') as f:
    result = get_result(f.read())
