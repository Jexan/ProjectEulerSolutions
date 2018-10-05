# Get the sum of the digits of factorial of 100.
# OPTIMAL (<0.1s)
#
# APPROACH:
#     Get the factorial, convert the number to string and sum all the digits.

from math import factorial

LIMIT = 100

def sum_fact_digits(n):
    return sum(map(int, str(factorial(n))))

result = sum_fact_digits(100)