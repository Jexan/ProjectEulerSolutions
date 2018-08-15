from sympy import sieve
from itertools import takewhile
from math import sqrt, floor

below = 50000000
 
limit_sq = floor(sqrt(below)) + 1
limit_cr = floor(below**(1/3)) + 1
limit_fr = floor(below**(1/3)) + 1

sief = list(sieve.primerange(0, limit_sq))

squared_primes = list(map(lambda x: x**2, sief))
cubed_primes = list(map(lambda x: x**3, takewhile(lambda x: x < limit_cr, sief)))
fourd_primes = list(map(lambda x: x**4, takewhile(lambda x: x < limit_fr, sief)))

genererated = set()

for i in squared_primes:
	print('Vamos por' + str(i))
	for j in cubed_primes:
		for k in fourd_primes:
			genererated.add(i+j+k)

print(list(genererated)[:10])
l = list(filter(lambda x: x < below, genererated))

result = len(l)
if __name__ == '__main__':
    print(result)