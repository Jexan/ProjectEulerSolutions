# Find the value of d < 1000 for which  1 / d contains the longest recurring cycle in its decimal fraction part.
# NORMAL (<1.2s)
# 
# APPROACH:
#   Get the possible denominators (the ones that doesn't get exact divisions) and exclude
#   the multiples of 3 (always has one digit cycle).
#   
#   A division can render other number not gotten before until a division yields a prevously obtained remainder,
#   in such case, from now on the chain will repeat itself. In the code that's how the chain length is obtained.

DUMMY_DENOMINATOR = 7
DUMMY_RESULT = 6

def generate_cycles():
    len_cycle = {} 
    for i in range(1, 1000, 2):
        # When divided by 3, the cycle tends to be of length 1
        if i % 3 == 0:     continue

        # Exact Division is not cyclic
        if 1000000 % i == 0: continue

        used_remainders = []
        remainder = 1

        while True:
            remainder %= i

            if remainder in used_remainders:
                # Gets from the first appearence of the remainder, to avoid
                # the non-chaining digits.
                len_cycle[i] = len(used_remainders[used_remainders.index(remainder):])
                break       
            else:
                used_remainders.append(remainder)            
                remainder *= 10

    return len_cycle

def max_cycle(len_cycle):
    return max(len_cycle, key=lambda x: len_cycle[x])

len_cycle = generate_cycles()

assert len_cycle[DUMMY_DENOMINATOR] == DUMMY_RESULT
result = max_cycle(len_cycle)