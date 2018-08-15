# Prime factorization by powers
def get_factors_count(n):
    factors  = defaultdict(dict)
    
    for i in sieve:
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

# Gets a list of factors, including repeated
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

# Get the unique divisors of a number. Needs a defaultdict
def produce_divs(n):
    n_factors = get_factors(n).copy()
    org_len = len(n_factors)
    n_factors += [1]*org_len

    return set(reduce(mul, i) for i in combinations(n_factors, org_len)).difference((n,))