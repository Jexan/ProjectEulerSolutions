# Pythagorean triple such that a + b + c = 1000
# OPTIMAL (<0.05s)
# 
# APPROACH:
#   Generate Pythagorean Triplets perimeters (see E075.py for better explanation), 
#   until one of them produce a perimeter of 1000, then just yield the product of the
#   sides.
#   
# NOTES:
#   - The brute force approach took 0.8 seconds to run.
#   - The method used here is a modified version of helpers.get_triangle_perimeters,
#   optimized for the tak at hand.

from math import gcd

LIMIT = 1000
def find_pythagorean_triple():
    for a in range(1, 11):
        for b in range(1, a):
            if gcd(a, b) != 1 or (a % 2 and b % 2):
                continue

            perimeter = 2*(a**2 + a*b)
            if perimeter > LIMIT: break

            times = LIMIT // perimeter 
            for i in range(1, times+1):
                if perimeter*i == LIMIT:
                    return i**3*(a**2-b**2)*(2*a*b)*(a**2+b**2)

result = find_pythagorean_triple()