from sympy       import sieve
from collections import defaultdict
from itertools   import combinations_with_replacement
from functools   import reduce

divisors_sieve = defaultdict(list)

def is_abundant(n):
    return sum(divisors_sieve[n]) > n

for x in range(1, 28124//2 + 1):
    for y in range(x*2, 28124, x):
        divisors_sieve[y].append(x) 

abundants = filter(is_abundant, range(1, 28124))
summable  = set(sum(i) for i in combinations_with_replacement(abundants, 2))

result = sum(set(range(1, 28124)).difference(summable))
if __name__ == '__main__':
    print(result)