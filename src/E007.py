# Find the 10001st prime
# SLOW (<6s)
# 
# APPROACH:
#   Basically use a sieve algorithm, expanding itself (the reason of why it is so slow).

from .helpers import generate_primes
from itertools import islice

DUMMY_NTH = 6 
DUMMY_RESULT = 13

NTH = 10001 

def get_nth_prime(n):
    return next(islice(generate_primes(), n-1, None))

assert get_nth_prime(DUMMY_NTH) == DUMMY_RESULT
result = get_nth_prime(NTH)