# Get the minimal |p_j - p_k| such that p_j, p_k, p_j+p_k + |p_j - p_k| are pentagonal
# VERY SLOW (~20s)
# 
# APPROACH:
#   Generate the pentagonal numbers, check their difference and keep track of the minimal diference.
#   Once p_(j+1) - p_j > minimal, break, since there will not be a lesser difference.

from itertools import count
from .helpers import take
from math import sqrt, modf

def generate_pent():
    result = 1
    for i in count(1):
        yield result
        result += 3*i + 1

def is_pent(n):
    fractional, integer = modf(sqrt(1+24*n))

    return fractional == 0 and not (integer + 1) % 6

def get_min_diff():
    pents = set()
    possible = set()
    minimal = float('inf')
    last_pent = 0

    for pent in generate_pent():
        to_remove = set()
    
        for i in pents:
            subs = pent - i 
            if subs < minimal and subs in pents and is_pent(pent + i):
                result = subs
                minimal = subs
            elif subs > minimal:
                to_remove.add(i)

        if minimal < pent - last_pent:
            return result

        pents.add(pent)
        pents -= to_remove
        last_pent = pent

result = get_min_diff()