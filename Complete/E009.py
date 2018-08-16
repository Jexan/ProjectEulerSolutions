# Pythagorean triple such that a + b + c = 1000

from itertools import takewhile

def find_pythagorean_triple():
    squares = set(i**2 for i in range(1000))

    for a in range(1, 1000):
        for b in range(a, 999 - a):
            c = (a**2 + b**2)**.5

            if a + b + c == 1000:
                return int(a*b*c)

result = find_pythagorean_triple()