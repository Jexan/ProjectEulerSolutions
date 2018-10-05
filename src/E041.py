# Get the first n-digit pandigital prime.
# FAST (<1.1s)
# 
# APPROACH:
#   - Use the permutations that are genererated by itertools.permutation
#     to generate them sorted.
#   - Generate primes only until sqrt(987654321), the max possible n-digit pandigital prime,
#     so it can be checked that the numbers are prime. 

from .helpers import primes_until
from itertools import permutations
from math import floor

limit = floor(987654321 ** .5)
primes = tuple(primes_until(limit))[3:]

def transform_to_num(t):
    return int(''.join(t))

def is_prime(n):
    if not n % 3:
        return False

    bound = floor(n**.5)
    for p in primes:
        if p > bound:
            return True
        elif not n % p:
            return False

def get_result():
    for n in range(9, 3, -1):
        for i in permutations(str(s) for s in range(n, 0, -1)):
            if i[-1] in '24685': continue
            if is_prime(transform_to_num(i)): 
                return transform_to_num(i)

result = get_result()