from sympy     import sieve
from itertools import count, product, chain

possible_a = range(-999, 1000, 2)
possible_b = chain(sieve.primerange(1,1000), (-p for p in sieve.primerange(1,1000)))

possible = product(possible_a, possible_b)

current_runners = possible
next_runners = []

for n in count(1):
    n2 = n**2

    for a, b in current_runners:
        if abs(n2 + a*n + b) in sieve:
            next_runners.append((a,b))

    if len(next_runners) <= 1:
        break

    current_runners, next_runners = next_runners, []

print(next_runners[0][0]*next_runners[0][1])