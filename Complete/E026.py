# Find the value of d < 1000 for which  1 / d contains the longest recurring cycle in its decimal fraction part.

len_cycle = {} 

DUMMY_DENOMINATOR = 7
DUMMY_RESULT = 6

def generate_cycles():
    for i in range(1, 1000):
        # When divided by 3, the cycle tends to be of length 1
        if i % 3 == 0:     continue

        # Exact Division is not cyclic
        if 1000000 % i == 0: continue

        possible_divisors = []
        remainder = 1

        while True:
            remainder %= i

            if remainder in possible_divisors:
                len_cycle[i] = len(possible_divisors[possible_divisors.index(remainder):])
                break       
            else:
                possible_divisors += [remainder]            
                remainder *= 10

def max_cycle():
    return max(len_cycle, key=lambda x: len_cycle[x])

generate_cycles()

assert len_cycle[DUMMY_DENOMINATOR] == DUMMY_RESULT
result = max_cycle()