from collections import defaultdict

factors = defaultdict(list)
primes = [2, 3]

def primes_until(n):
    sieve = {}
    
    yield 2
    for i in range(3, n, 2):
        if sieve.get(i):
            continue

        yield i
        primes.append(i)

        for j in range(i**2, n, i):
            sieve[j] = True 

# Prime factorization by powers
def get_factors_count(n):
    factors  = defaultdict(dict)
    
    for i in primes_until(n):
        if n == i:
            factors[n][i] = 1 
        elif not n % i:
            div = n//i

            if not factors[div]:
                get_factors(div)

            factors[n] = factors[div].copy()
            factor_ref = factors[n]

            if factor_ref.get(i):
                factor_ref[i] += 1
            else:
                factor_ref[i] = 1
        else:
            continue

        return factors[n]

# Gets a list of unique prime factors
def get_factors(n):
    sqrt_n = int(n**.5)
    for i in primes_until(sqrt_n):
        if not n % i:
            yield i

# Get the unique divisors of a number. Needs a defaultdict
def produce_divs(n):
    n_factors = get_factors(n).copy()
    org_len = len(n_factors)
    n_factors += [1]*org_len

    return set(reduce(mul, i) for i in combinations(n_factors, org_len)).difference((n,))

# Generate fibonnacci numbers
def generate_fibonnacci():
    prev, current = 0, 1

    while True:
        yield current

        prev, current = current, prev + current
        