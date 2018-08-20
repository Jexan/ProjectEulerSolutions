# Pandigital of the concat of products of n by (1, 2... k)
# OPTIMAL
# 
# APROACH:
#   The info gives 918273645 as possible solution, so the solution must be higher than that.
#   Also, n must be higher thatn 12 since 9 gets the higer pandigital
#   of the one digit numbers, but it's not the solution. It must be lower thatn 9876, since if n is a 5 digit
#   number, str(n*1) + str(n*2) has at least length 10, so it cannot be a pandigital.
#   
#   By all this info, the n must start with a 9, since the first digits of the pandigital will always be n. 
#   If n starts with 8 or lower, any pandigital number will be lower than 918273645.

from itertools import repeat, chain, count, permutations
from .helpers import digits

highest = '918273645'

def get_max_pandigital():
    two_digits = (''.join(per) for per in zip(repeat('9'), '12345678'))
    three_digits = (''.join(('9', *per)) for per in permutations('12345678', 2))
    four_digits = (''.join(('9', *per)) for per in permutations('12345678', 3))

    max_so_far = 0

    for i in chain(two_digits, three_digits, four_digits):
        remaining_digits = set(digits)
        number = int(i)

        for n in count(1):
            product = number * n
            product_str = str(product)
            product_digits = frozenset(product_str)

            if len(product_digits) < len(product_str) or product_digits - remaining_digits:
                break

            if remaining_digits == product_digits:
                pandigital = int(''.join(str(number * n) for n in range(1, n+1)))
                if max_so_far < pandigital:
                    max_so_far = pandigital
                break

            remaining_digits -= product_digits

    return max_so_far

result = get_max_pandigital()