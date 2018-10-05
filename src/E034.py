# Sum all numbers whose sum of digits factorial is equal to themselves
# SLOW (<16s)
# 
# APPROACH:
#   Reduce the possible suspects checking which numbers are imposible to craft
#   with the sum of factorials. Still, most numbers can't be reduces in a obvious,
#   straightforward way.

from math import factorial
from itertools import chain, permutations, combinations_with_replacement, product

DUMMY_NUM = '145'

factorials = [factorial(i) for i in range(10)]

def better_range():
    for i in range(120, 240):
        if i % 100 > 66:
            continue
        if i % 10 > 6:
            continue
        yield str(i)   

    for i in range(1440, 1561):
        if i % 100 > 77:
            continue
        if i % 10 > 7:
            continue
        yield str(i)

    for i in chain(range(5047, 7666), range(10177, 15841)):
        if i % 1000 > 770:
            continue
        if i % 100 > 88:
            continue
        if i % 10 > 8:
            continue
        yield str(i)

    for i in range(factorial(8), factorial(8)*5):
        str_nu = str(i)
        if '8' not in str_nu or '9' in str_nu:
            continue
        yield str_nu

    for i in range(factorial(9), 1799999):
        str_nu = str(i)
        if '9' not in str_nu:
            continue
        yield str_nu

def digit_factorials_sum(n):
    return sum(factorials[int(i)] for i in n)

def find_criterion_numbers():
    return sum(int(i) for i in better_range() if digit_factorials_sum(i) == int(i))

assert digit_factorials_sum(DUMMY_NUM) == int(DUMMY_NUM)
result = find_criterion_numbers()