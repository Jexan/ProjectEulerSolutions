# sum of the digits of 2**1000
# OPTIMAL (0.1s)
# 
# APPROACH:
#   A brute force approach. It's quite fast that way, so no need to optimize.

DUMMY_EXPONENT = 15
DUMMY_RESULT = 26

EXPONENT = 1000

def sum_digits_n_power_of_2(exponent):
    return sum(int(digit) for digit in str(2**exponent))

assert sum_digits_n_power_of_2(DUMMY_EXPONENT) == DUMMY_RESULT
result = sum_digits_n_power_of_2(EXPONENT)