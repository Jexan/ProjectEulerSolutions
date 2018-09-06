from collections import defaultdict, Counter
from itertools import combinations, islice, takewhile, chain

factors = defaultdict(list)
primes = [2]

sieve_generators = {}

digits = frozenset('123456789')

def do_times(n, iterable):
    counter = 0
    while counter < n:
        counter += 1
        next(iterable, None)

def find(f, iterable):
    for i in iterable:
        if f(i): return i

def generate_primes():
    sieve = {}
    yield 2
    
    _from = 2
    limit = 1000002
    step = 1000000

    def min_gen():
        for i in range(_from + 1, limit, 2):
            if sieve.get(i):
                continue

            yield i
            primes.append(i)

            sieve_generator = prepare_for_sieve(i, sieve)
            times_to_run = limit // i

            do_times(times_to_run, sieve_generator)
            sieve_generators[i] = sieve_generator

    while True:
        for i in min_gen():
            yield i

        _from = limit
        limit += step 

        for prime, sieving_fun in sieve_generators.items():
            do_times(limit//prime, sieving_fun)

def prepare_for_sieve(n, sieve):
    current = n**2

    while True:
        sieve[current] = True
        yield
        current += n 

def primes_until(n):
    sieve = {}
    
    yield 2
    for i in range(3, n, 2):
        if sieve.get(i):
            continue

        yield i

        for j in range(i**2, n, i):
            sieve[j] = True 

class SieveClass:
    primes = set()
    biggest_primes = 2

    def __init__(self):
        self.prime_gen = self.get_prime_gen()

    def __contains__(self, item):
        return item in self.primes

    def __iter__(self):
        return chain(primes, self.prime_gen)

    def get_prime_gen(self):
        for prime in generate_primes():
            self.biggest_primes = prime
            self.primes.add(prime)

            yield prime

sieve = SieveClass()

def is_palindrome(n):
    word_n = str(n)

    return word_n == word_n[::-1]

def find_palindromes(lower_lim, upper_lim):
    palind_range = (i for i in range(lower_lim, upper_lim) if i % 10) # numbers that end in 0 are never palindromes

    for n1, n2 in combinations(palind_range, 2):
        result = n1*n2

        if is_palindrome(result):
            yield result

def prime_factorization(n):
    for prime in primes_until(int(n**.5) + 1):
        if not n % prime:
            div = n // prime

            return [prime] + prime_factorization(div)

    return [n]

def get_factors_number(n):
    return Counter(prime_factorization(n))

def mcm(*xs):
    factors = [get_factors_number(x) for x in xs]
    factors_with_max_exponent = {}

    for counter in factors:
        for prime, times in counter.items():
            saved_factor = factors_with_max_exponent.get(prime)

            if saved_factor is None or saved_factor < times:
                factors_with_max_exponent[prime] = times

    result = 1
    for prime, times in factors_with_max_exponent.items():
        result *= prime**times

    return result

def consecutive_iter(iterator, size=2):
    iterator = tuple(iterator)
    max_index = len(iterator) - 1 
    
    current_index = 0

    while current_index + size <= max_index: 
        yield iterator[current_index:current_index + size]
        current_index += 1
    

# Prime factorization by powers
def get_factors_count(n):
    factors  = defaultdict(dict)
    
    for i in primes_until(int(n**.5)):
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

# Generate fibonacci numbers
def generate_fibonacci():
    prev, current = 0, 1

    while True:
        yield current

        prev, current = current, prev + current

def take(n, iterable):
    return islice(iterable, n)