# Get the first number that fails the Golbach Conjeture
# NORMAL (4 seconds)
# 
# APPROACH:
#   Brute force approach. Check if a set created by substracting the number by every prime
#   has an element in common with the twice squares. The first one that doesnt is a number
#   that can't be written by Golbach's way.

from .helpers import take, generate_primes
from itertools import count, takewhile

double_squares_gen = (2*i**2 for i in count(0))
primes_gen = generate_primes()

def find_number():
    primes = set()
    double_squares = set()
    step = 10000
    initial = 33
    last_prime = 1

    while True:
        double_squares |= set(take(int(step*.5), double_squares_gen))

        for i in range(initial, initial + step, 2):
            while i > last_prime:
                last_prime = next(primes_gen)
                primes.add(last_prime)

            if i in primes:
                continue

            if not frozenset(i - p for p in primes) & double_squares:
                return i
        
        initial += step 
                
result = find_number()