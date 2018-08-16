# Sum of pandigital numbers with given prop
from itertools import permutations

DUMMY_PANDIGITAL = '1406357289'

num_set = frozenset('0123456789')
five_endings = frozenset('05')
two_endings = frozenset('02468')
primes = (2, 3, 5, 7, 11, 13, 17)
multiples_of_17 = (17*i for i in range(1, 1000//17))

pandigitals = []

def unique_digits(n):
    str_n = str(n)

    return len(frozenset(str_n)) == len(str_n)

def get_possible_with(n, available_nums, pandigital):
    possible = []

    for num in available_nums:
        mul_n = int(num + pandigital[:2])

        if not mul_n % n:
            possible.append(num)

    return possible
        
to_be_used_17_muls = map(lambda x: '{:0=3}'.format(x), filter(unique_digits, multiples_of_17))

def find_mult(prime_index, current_nums, pandigital):
    prime = primes[prime_index]

    if prime_index < 0:
        valid_begins = (''.join(per) for per in permutations(current_nums))

        for i in valid_begins:
            pandigitals.append(i + pandigital)

        return

    for pos in get_possible_with(prime, current_nums, pandigital):
        find_mult(prime_index - 1, current_nums - frozenset(pos), pos + pandigital)     

def generate_pandigital():
    for mul_17 in to_be_used_17_muls:
        find_mult(5, num_set - frozenset(mul_17), mul_17)

generate_pandigital()

assert DUMMY_PANDIGITAL in pandigitals
result = sum(int(n) for n in pandigitals)