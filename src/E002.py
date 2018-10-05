# Sum even fibonacci under 4 million
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Just produce the fibonaccis with an efficient (recursion-free) generator
#   and sum them.

from .helpers import generate_fibonacci

LIMIT = 4000000

def sum_even_fibb_until(limit):
    def mini_gen():
        for n in generate_fibonacci():
            if n >= limit:
                return

            if not n % 2:
                yield n

    return sum(mini_gen())

result = sum_even_fibb_until(LIMIT)