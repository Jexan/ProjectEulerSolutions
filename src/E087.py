# How many numbers can be expressed as p1**2 + p2**3 + p3**4 below 5.000.000
# SLOW (<3s)
# 
# APPROACH:
#   Brute force + bounding the primes. If n > sqrt 5e7, n**2 > 5e7 and will not work for the criteria.

from .helpers import primes_until
from itertools import takewhile
from math import sqrt, floor

below = 50000000

def get_numbers_quantity():
    limit_sq = floor(sqrt(below)) + 1
    limit_cr = floor(below**(1/3)) + 1
    limit_fr = floor(below**.25) + 1

    sieve = tuple(primes_until(limit_sq))

    # For some reason if the two last two primes collection is not tuplefied, 
    # the primes are not going to be yielded correctly.
    squared_primes = (i**2 for i in sieve)
    cubed_primes = tuple(j**3 for j in takewhile(lambda x: x < limit_cr, sieve))
    fourth_primes = tuple(k**4 for k in takewhile(lambda x: x < limit_fr, sieve))

    return len(set(filter(lambda x: x < below, (i + j + k for i in squared_primes for j in cubed_primes for k in fourth_primes))))

result = get_numbers_quantity()