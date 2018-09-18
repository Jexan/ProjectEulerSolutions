# Number of irreductible fractions between 1/2, 1/3 such that the denomiator is not greater than 12000
# SLOW (<13s)
# 
# APPROACH:
#   Basically brute force. Remembering than if n/d is between 1/2 and 1/3 then:
#           2n < d < 3n

from math import gcd

limit = 12000 + 1

def get_result(limit):
    max_numerator = limit // 2

    lower_den_step = 2
    upper_den_step = 3

    lower_den = 5
    upper_den = 6

    counter = 0
    for n in range(2, max_numerator):
        step = 1
        if not n % 2:
            step = 2 

        for d in range(lower_den, min(limit, upper_den), step):
            if gcd(n, d) == 1:
                counter += 1

        lower_den += lower_den_step
        upper_den += upper_den_step

    return counter

result = get_result(limit)