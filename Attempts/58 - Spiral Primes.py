from math import inf, floor, sqrt
from sympy import sieve
from itertools import dropwhile

def generate_numbers(limit=inf):
    current = 1
    internal_square = 1
    steps = 0

    drop_count = 0

    while internal_square <= limit:
        drop_count += 1
        
        if not drop_count % 5:
            continue

        yield current
        if current == internal_square**2:
            internal_square += 2
            steps += 2

        current += steps

number_of_primes = 0
number_of_diagonals = 0

for i in dropwhile(lambda x: x==1, generate_numbers()):
    if i in sieve:
        number_of_primes += 1

    number_of_diagonals += 1

    if number_of_primes/number_of_diagonals <= .10:
        print(number_of_diagonals)
        print(i)
        break