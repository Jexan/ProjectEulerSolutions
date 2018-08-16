# Sum of primes under 2 million

from .helpers import generate_primes
from itertools import takewhile

LIMIT = 2000000

DUMMY_LIMIT = 10
DUMMY_RESULT = 17

def sum_primes_below(limit):
    return sum(takewhile(lambda x: x < limit, generate_primes()))

assert sum_primes_below(DUMMY_LIMIT) == DUMMY_RESULT
result = sum_primes_below(LIMIT)