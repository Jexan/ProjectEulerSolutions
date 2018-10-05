# Number of irreductible fractions with denominator < 1000000
# SLOW (<5s)
# 
# APPROACH:
#   - If d is the denominator, the number of irreductible fraction with numerator lower than
#       d is exactly totient(d).
#   - Find the sum of all the totients values under 1000000
#   - Make use of the totient product formula:
#       totient(n) = n*product(1 - 1/p for p in unique_primes_that_factorizes_n)

from .helpers import produce_totients_list

limit = 1000000 + 1 # Since it is lower or equal than it
result = int(sum(produce_totients_list(limit)))