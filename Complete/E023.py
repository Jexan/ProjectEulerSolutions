# Sum of all numbers that cannot be written as sum of two abundant number
# Slow (20 seconds)

from collections import defaultdict
from itertools   import combinations_with_replacement

divisors_sieve = defaultdict(list)

def is_abundant(n):
    return sum(divisors_sieve[n]) > n

def get_abudant():
    for x in range(1, 28124//2 + 1):
        for y in range(x*2, 28124, x):
            divisors_sieve[y].append(x) 

    return filter(is_abundant, range(1, 28124))

def get_sum_non_abudant_sum_numbers():
    return sum(frozenset(range(1, 28124)) - frozenset(map(sum, combinations_with_replacement(get_abudant(), 2))))

result = get_sum_non_abudant_sum_numbers()