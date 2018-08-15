# Biggest palindrome formed by a product of two 3 digits number

from .helpers import find_palindromes

DUMMY_DIGITS = 2
DUMMY_RESULT = 9009

DIGITS = 3

def find_biggest_palindrome(digits):
    lower_lim = 10 ** (digits - 1)
    upper_lim = 10 * lower_lim

    return max(find_palindromes(lower_lim, upper_lim))

assert find_biggest_palindrome(DUMMY_DIGITS) == DUMMY_RESULT
result = find_biggest_palindrome(DIGITS)