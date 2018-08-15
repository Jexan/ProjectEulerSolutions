from itertools import permutations
from functools import reduce
from operator import add

sieve = [2,3,5,7,11,13,17]

permuts = (reduce(add, i) for i in permutations('0123456789'))

def criterion(n):
	for i in range(2, 9):
		if int(n[i-1:i+2]) % sieve[i-2]:
			return False
	return True

assert(criterion('1406357289'))
assert(not criterion('1111111111'))

valid = list(map(int, filter(criterion, permuts)))

print(valid, sum(valid))