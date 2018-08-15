# Lowest evenly divisible by all from 1 to 20

from .helpers import mcm

DUMMY_TO = 10
DUMMY_RESULT = 2520

TO = 20

def min_multiple(to):
    return mcm(*range(1, to + 1))

assert min_multiple(DUMMY_TO) == DUMMY_RESULT
result = min_multiple(TO)