from collections import defaultdict, Counter
from itertools   import combinations, starmap

factors = defaultdict(list)

def get_factors(n):
    if factors[n]:
        return factors[n]

    for i in sieve:
        if n == i:
            factors[n] += [i] 
        elif not n % i:
            div = n//i

            if not factors[div]:
                get_factors(div)

            factors[n] += factors[div].copy() + [i]
        else:
            continue

        return factors[n]

def have_unique_factors_n(n, factors=4):
    return len(set(get_factors(n))) == factors

def distinct_factors(n1, n2):
    n1, n2 = Counter(get_factors(n1)), Counter(get_factors(n2))
    n1.subtract(n2)

    for k, v in n1.items():
        if not v: return False

    return True

current = 10

while True:
    if have_unique_factors_n(current):
        if all(map(have_unique_factors_n, range(current+1, current+4))):
            if all(starmap(distinct_factors, combinations(list(range(current, current+4))))):
                print(current)
                break
    else:
        current += 1
