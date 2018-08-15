from math import sqrt, floor

limit = 10000
sum_factors = {}
amicable_numbers = []

def get_factors(n):
	divisors = []
	square = floor(sqrt(n))
	for i in range(2, square):
		if n%i == 0:
			divisors.extend([i, n//i])
	divisors.append(1)
	return divisors

for i in range(2, limit):
	if i in sum_factors: continue

	divisor_sum = sum(get_factors(i))
	if divisor_sum in sum_factors:
		other_divisor_sum = sum_factors[divisor_sum]
	else:
		other_divisor_sum = sum(get_factors(divisor_sum))
		sum_factors[divisor_sum] = other_divisor_sum

	if other_divisor_sum == i and divisor_sum != i:
		amicable_numbers.extend([divisor_sum, other_divisor_sum])

print(sum(set(amicable_numbers)), len(amicable_numbers), set(amicable_numbers))