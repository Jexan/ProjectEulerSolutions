# Get the n su ch that n/totient(n) is maximixed for n <= 1.000.000 
# NORMAL (<4s)
# 
# APPROACH:
#   - We make use of the formula:
#       totient(n) = n*product(1 - 1/p for p in unique_primes_that_divide_n)
#     So:
#       totient(n)/n = product(1 - 1/p for p in unique_primes_that_divide_n)
#     In that case, it is easy to prove that:
#       min(totient(n)/n) == max(n/totient(n)) (n <= 1e6)
#       
#   - Using the formula, we keep track the product of unique primes of numbers under 1e6,
#     with an approach similar to the Sieve algorithm.

from .helpers import primes_until

limit = 1000000 + 1

def produce_totient_n_div_n(limit):
    totients = [1] * limit

    for prime in primes_until(limit):
        result = 1 - 1/prime
        for i in range(prime, limit, prime):
            totients[i] *= result

    return totients

totients = produce_totient_n_div_n(limit)
result = totients.index(min(totients)) 