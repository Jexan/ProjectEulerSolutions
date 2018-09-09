# Get the simplified denominator of the product of the four "incidental" fractions n/d with n, d in [10..99] 
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   - Generate the single fractions (n/d with 1 <= n < d < 9).
#   - Generate the multiples (m*(n/d)).
#   - Check if the multiples' denominator and numerator has a common digit (that is not 0).
#   - If the multiples are equal to the single fractions that generated them, we got a criteria-fitting fraction.

from math import ceil, gcd
from functools import reduce
from .helpers import take

def simplify_rational(n):
    num, den = n

    factor = gcd(*n)
    return num // factor, den // factor

def gen_fractions():
    for n in range(1, 10):
        for d in range(n+1, 10):
            yield (n, d)

def gen_multiples(frac):
    num, den = frac
    first_mult = ceil(10 / num)
    last_mult = ceil(100 / den)

    for mult in range(first_mult, last_mult):
        yield num*mult, den*mult

def get_other(value, string):
    index = string.index(value)
    return string[0 if index == 1 else 1]

def get_removables():
    fracs_multiples = {frac: tuple(gen_multiples(frac)) for frac in gen_fractions()}
    zero_set = frozenset('0')

    for (og_num, og_den), multiples in fracs_multiples.items():
        for num, den in multiples:
            str_num = str(num)
            str_den = str(den)
            common_digit = set(str_num) & set(str_den)

            if not common_digit or common_digit == zero_set: continue

            common_digit = common_digit.pop()

            if common_digit == '0': continue

            if og_num*int(get_other(common_digit, str_den)) == og_den*int(get_other(common_digit, str_num)):
                yield num, den

removable_fracs = frozenset(get_removables())
frac_product = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), removable_fracs)

result = simplify_rational(frac_product)[1]