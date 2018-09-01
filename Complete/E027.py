# Get the numbers -1000 < a, b < 1000 such that n^2 + a*n + b produces more
# consecutive primes.
# OPTIMAL
#
# APPROACH: 
#     Produce all the possible a, b, noting that b's must be primes (since 0**2 + 0*1 + b = b must be prime).
#     Then we check with every possible n starting with 1, to check which combinations yield primes
#     Those who don't are discarded. We keep on, until only one combination remains, which will be the one that produced the most
#     primes.

from .helpers  import primes_until
from itertools import count, product, chain

def get_max_combination():
    possible_a = range(-999, 1000, 2)
    primes = frozenset(primes_until(1000))
    possible_b = chain(primes, (-p for p in primes))

    possible = product(possible_a, possible_b)

    current_runners = possible
    next_runners = []

    for n in count(1):
        n2 = n**2

        for a, b in current_runners:
            if abs(n2 + a*n + b) in primes:
                next_runners.append((a,b))

        if len(next_runners) <= 1:
            return next_runners[0]

        current_runners, next_runners = next_runners, []

a, b = get_max_combination()
result = a*b