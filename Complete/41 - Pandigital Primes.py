from sympy import sieve
from itertools import takewhile

def create_sieve(n):
	sieve = [i for i in range(n)]
	for i in sieve[2:]:
		if i and (i*i < n):
			for j in range(i*i,n, i):
				if (j >= n): break

				sieve[j] = 0
	return [i for i in filter(lambda x: x!= 0, sieve)][1:]

def pandigital(n, s):
	for j in range(1, len(s) + 1):
		if str(j) not in s:
			return False

	return True

n = 10000000

bound_sieve = list(takewhile(lambda x: x < n, sieve))
max_prime = 0

for i in reversed(bound_sieve):
	s = str(i)
	print('Evaluando:' + str(i))

	if '0' in s: 
		continue

	prime = set(s)

	if len(prime) < len(s):
		continue
	
	if pandigital(n,s): 
		max_prime = i
		break

result = max_prime
if __name__ == '__main__':
    print(result)