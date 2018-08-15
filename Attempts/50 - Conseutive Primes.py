from sympy import sieve
from itertools import takewhile

n = 100
bound_sieve = list(takewhile(lambda x: x < n, sieve))
