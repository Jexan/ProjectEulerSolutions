# Difference between sum of squares of the first 100 numbers and squares of the sum of the first 100
# OPTIMAL(<0.1s)
# 
# APPROACH:
#   Basically brute force, using generators, ranges and sums.

DUMMY_LIMIT = 10
DUMMY_RESULT = 2640

LIMIT = 100

def sum_difference(limit):
    return sum(range(1, limit+1))**2 - sum(n**2 for n in range(1, limit + 1)) 

assert sum_difference(DUMMY_LIMIT) == DUMMY_RESULT
result = sum_difference(LIMIT) 