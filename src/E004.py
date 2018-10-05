# Biggest palindrome formed by a product of two 3 digits number
# NORMAL (<1.3s)
# 
# APPROACH:
#   Basically generate every product of numbers between 100 and 1000, 
#   excluding numbers that ends with a 0

from .helpers import is_palindrome
from itertools import combinations

DUMMY_DIGITS = 2
DUMMY_RESULT = 9009

DIGITS = 3

def find_palindromes(lower_lim, upper_lim):
    palind_range = (i for i in range(lower_lim, upper_lim) if i % 10) # numbers that end in 0 are never palindromes

    for n1, n2 in combinations(palind_range, 2):
        result = n1*n2

        if is_palindrome(result):
            yield result

def find_biggest_palindrome(digits):
    lower_lim = 10 ** (digits - 1)
    upper_lim = 10 * lower_lim

    return max(find_palindromes(lower_lim, upper_lim))

assert find_biggest_palindrome(DUMMY_DIGITS) == DUMMY_RESULT
result = find_biggest_palindrome(DIGITS)