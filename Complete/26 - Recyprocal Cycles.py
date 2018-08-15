len_cycle = {} 

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

result = max(len_cycle, key=lambda x: len_cycle[x])
if __name__ == '__main__':
    print(result)