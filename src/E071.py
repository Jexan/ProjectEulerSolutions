# Find the d of the irreducible fraction n/d where d < 1e6 and n/d is the closest left fraction to 3/7.
# SLOW (<6s)
# 
# APPROACH:
#   - It is evident that the fraction must be between 2/7 and 3/7.
#   - We can just generate n's for n/ 1000000 and then, if it's the closest number so far
#   to 3/7, check if it is irreductible.
#   - Let c be the closest number to 3/7 so far, then the denominator d must fulfil:
#       n/c > d > 7n/3 (n is the numerator)
#      Reducing greatly the possible denominators to check.

from math import floor, ceil, gcd

upper_bound = 3/7
lower_bound = 2/7
limit = 1000000

max_numerator = floor(limit * upper_bound)

closest = lower_bound
closest_numerator = 0

step_lower_den = 1/upper_bound
step_upper_den = 1/lower_bound
lowest_den = step_lower_den
highest_den = step_upper_den

for n in range(2, max_numerator):
    highest_den += step_upper_den
    lowest_den += step_lower_den

    for d in range(floor(lowest_den), floor(highest_den)):
        division = n/d

        if closest < division and division < upper_bound and gcd(n, d) == 1:            
            closest = division 
            closest_numerator = n
            
            step_upper_den = 1/division
            lowest_den = n*step_upper_den

result = closest_numerator