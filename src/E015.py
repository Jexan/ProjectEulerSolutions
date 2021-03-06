# Number of possible ways in a Lattice path
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   A combinatorial formula is used. 

from math import factorial

DUMMY_DIMENSION = 2
DUMMY_RESULT = 6

DIMENSION = 20

def lattices(n):
	return int(factorial(2*n)/(factorial(n)**2))

assert lattices(DUMMY_DIMENSION) == DUMMY_RESULT
result = lattices(DIMENSION)