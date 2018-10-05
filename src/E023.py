# Sum of all numbers that cannot be written as sum of two abundant number
# SLOW (<20s)
# 
# APPROACH:
#   Store the divisors sum in a list then filter it to get the abundant numbers.
#   After it, yield the sums.

def get_abudant():
    divisors_sieve = [0]*28125

    def is_abundant(n):
        return divisors_sieve[n] > n
    
    for x in range(1, 28124//2 + 1):
        for y in range(x*2, 28124, x):
            divisors_sieve[y] += x 

    return (index for index, i in enumerate(divisors_sieve) if index < i)

def yield_abudant():
    abundant = tuple(get_abudant())
    for x in abundant:
        for y in abundant:
            summation = x+y
            if summation > 28124:
                break

            yield summation

def get_sum_non_abudant_sum_numbers():
    return sum(frozenset(range(1, 28124)) - frozenset(yield_abudant()))

result = get_sum_non_abudant_sum_numbers()