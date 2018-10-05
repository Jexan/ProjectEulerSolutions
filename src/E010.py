# Sum of primes under 2 million
# SLOW (<2.1s)
# 
# APPROACH
#   Basically use a sieve to generate the primes and then sum them.

from .helpers import primes_until

LIMIT = 2000000

DUMMY_LIMIT = 10
DUMMY_RESULT = 17

def sum_primes_below(limit):
    return sum(primes_until(limit))

assert sum_primes_below(DUMMY_LIMIT) == DUMMY_RESULT
result = sum_primes_below(LIMIT)