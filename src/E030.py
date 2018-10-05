# Get the sum of the numbers whose sum of digits to the five power is equal to themselves.
# NORMAL(~3s)
# 
# APPROACH:
#   The result is brute forced, knowing some bounds:
#       - Since 1**5 and 2**5 are the only five powers with less than 3 digits, and 12, 21 does not fit the criteria, the lower bound is 100.
#       - Since 9.999.999 (7 digit) would have a 6 digit sum of five powers, the max bound is 1.000.000.

from itertools import takewhile, permutations

def get_criteria_nums():
    fifths = tuple(digits**5 for digits in range(0, 10))
    possible = {}
    results = set()

    for digits in range(3, 7):
        lower_bound = 10**(digits-1)
        max_bound = 10*lower_bound

        until = len(tuple(takewhile(lambda x: x < max_bound, fifths))) 

        for digits in permutations(range(0, until), digits):
            sum_digits = sum(fifths[n] for n in digits)
            
            if lower_bound < sum_digits < max_bound:
                tuple_digits_result = tuple(int(digits) for digits in str(sum_digits))

                digits_set = frozenset(digits)
                result_set = frozenset(tuple_digits_result)

                if digits_set == result_set:
                    if len(tuple_digits_result) == len(digits):
                        yield sum_digits

result = sum(get_criteria_nums())