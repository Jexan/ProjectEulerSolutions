# Find numbers that are triangular, pentagonal and hexagonal
# OPTIMAL 
# 
# APPROACH: 
# 	Solve the equalities of pentagonal, triangular and hexagonal number, getting two equations
# 	for the indeces of pentagonal and triangular.
# 	Since hexagonal index is free, we try with increasing values of the index until we get integer indeces. 

from itertools import count

DUMMY_INIT = 140
DUMMY_RESULT = 40755

INIT = 144

def pentagonal_index(triangular):
	return (1 + (1 + 12 * triangular * (triangular + 1))**.5) / 6

def triangular_index(hexagonal):
	return (-1 + (1 + 8 * hexagonal * (2 * hexagonal - 1))**.5) / 2

def pentagonal(n):
	return n*(3*n-1)/2

def generate_numbers_and_find_common(init_in):
	for i in count(init_in):
		triang = triangular_index(i)
		if int(triang) == triang:
			pent = pentagonal_index(triang)
			if int(pent) == pent:
				return pentagonal(int(pent))

assert generate_numbers_and_find_common(DUMMY_INIT) == DUMMY_RESULT
result = generate_numbers_and_find_common(INIT)