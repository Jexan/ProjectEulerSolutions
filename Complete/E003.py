# Largest prime factor of 600851475143

from .helpers import get_factors

DUMMY_TARGET = 13195
DUMMY_RESULT = 29

TARGET = 600851475143

def max_factor(n):
    return max(get_factors(n))

assert max_factor(DUMMY_TARGET) == DUMMY_RESULT
result = max_factor(TARGET)