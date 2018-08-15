def create_sieve(n):
	sieve = [i for i in range(n)]
	for i in sieve[2:]:
		if i and (i*i < n):
			for j in range(i*i,n, i):
				if (j >= n): break

				sieve[j] = 0
	return [i for i in filter(lambda x: x!= 0, sieve)][1:]

def circularize(n):
	prime = str(n)
	permutations = set()

	for i in range(1+len(prime)):
		permutations.add(prime[i:] + prime[:i])

	return map(int, permutations)

def circulars_are_prime(n):
	print('Checking prime:' + str(n))
	for i in circularize(n):
		if i not in sieve:
			return False
	return True

max_prime = 1000000

sieve = create_sieve(max_prime)
circulars = [i for i in filter(circulars_are_prime, sieve)]

result = len(circulars), circulars
if __name__ == '__main__':
    print(result)