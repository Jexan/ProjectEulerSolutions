# Get the 1.000.000 lexicographical permutation of the 10 digits.
# OPTIMAL
# 
# APPROACH:
#   Use a combinatory approach. For every digit, check, according to the factorial
#   value, which digit shall be used next 

from math import factorial

TEN_DIGITS = map(str, range(10))
LIMIT = 1000000

THREE_DIGITS = range(3)
DUMMY_POSITION = 4
DUMMY_RESULT = [1, 2, 0]

def get_nth_permutation(nth, iterable):
    list_values = list(iterable)
    seq = list()
    limit = nth

    for index in range(len(list_values), 0, -1):
        position, remainder = divmod(limit, factorial(index-1))
        
        # An exact division means that the previous number shall be used.
        if not remainder:
            position -= 1

        limit -= (position * factorial(index-1))
        value = list_values[position]
        
        list_values.remove(value)
        seq.append(value)

    return seq

assert get_nth_permutation(4, THREE_DIGITS) == DUMMY_RESULT
result = int(''.join(get_nth_permutation(LIMIT, TEN_DIGITS)))