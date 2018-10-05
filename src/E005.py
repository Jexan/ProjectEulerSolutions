# Lowest evenly divisible by all from 1 to 20
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   The lowest number evenly divisble from n in 1, 2, ..., 20
#   is exactly the minimal common multiple of the numbers from 1 to 20.
#   Using the basic algorithm "common and uncommon factors with max exponent",
#   it is trivial to find the answer.

from .helpers import mcm

DUMMY_TO = 10
DUMMY_RESULT = 2520

TO = 20

def min_multiple(to):
    return mcm(*range(1, to + 1))

assert min_multiple(DUMMY_TO) == DUMMY_RESULT
result = min_multiple(TO)