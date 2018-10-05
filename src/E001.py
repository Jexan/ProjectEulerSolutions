# Sum of multiples of 3 and 5
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Simple brute force is enough.

DUMMY_LIMIT = 10
DUMMY_RESULT = 23
LIMIT = 1000

def sum_multiples(limit):
    return sum(i for i in range(1, limit) if not i % 3 or not i % 5)

assert sum_multiples(DUMMY_LIMIT) == DUMMY_RESULT
result = sum_multiples(LIMIT)