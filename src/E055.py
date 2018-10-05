# How many Lychrel under 10.000?
# OPTIMAL (<0.5)
# 
# APPROACH:
#   Brute force. A number that produces no palindromes
#   after 50 cycles are Lychrel.

from .helpers import is_palindrome

def is_lychrel(n):
    current = n
    for i in range(50):
        result = current + int(str(current)[::-1])

        if is_palindrome(result):
            return False

        current = result

    return True

result = len(tuple(filter(is_lychrel, range(1, 10001))))