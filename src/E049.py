# Get the 12-digit concat of the primes such that p2-p1 == p3-p2 and p1, p2, p3 have permuted digits.
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Brute force. Make heavy use of sets to remove checked primes.  

from .helpers import primes_until, find
from itertools import dropwhile, permutations, combinations

def permute_n(n):
    return frozenset(int(''.join(per)) for per in permutations(str(n), 4))

def get_criteria_primes():
    relevant_primes = tuple(dropwhile(lambda x: x < 1000, primes_until(10000)))
    primes_set = set(relevant_primes)

    possible = []
    for prime in relevant_primes:
        if prime not in primes_set:
            continue

        possible_primes = permute_n(prime) & primes_set

        if len(possible_primes) >= 3:
            numbers = sorted(possible_primes)
        
            for triplet in combinations(numbers, 3):
                if triplet[1] - triplet[0] == triplet[2] - triplet[1]:
                    possible.append(triplet)

        primes_set -= possible_primes

    return possible

criteria_primes = get_criteria_primes()
IS_DUMMY_VALUE = lambda b: (lambda x: 1487 in x) if b else (lambda x: 1487 not in x)

assert find(IS_DUMMY_VALUE(True) , criteria_primes)
result = int(''.join(str(i) for i in find(IS_DUMMY_VALUE(False), criteria_primes)))