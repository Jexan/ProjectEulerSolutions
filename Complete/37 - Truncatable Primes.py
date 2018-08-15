from sympy import sieve

truncatables = []
truncatable_count = 0

for i in filter(lambda x: x > 10, sieve):
    str_prime = str(i)
    prime_length = len(str_prime)
    truncatable = True

    to_check_prime_length = prime_length - 1
    while to_check_prime_length > 0:
        truncatable = int(str_prime[to_check_prime_length:]) in sieve and int(str_prime[:to_check_prime_length]) in sieve
        
        if not truncatable:
            break

        to_check_prime_length -= 1

    if truncatable:
        truncatables.append(i)
        truncatable_count += 1

        if truncatable_count == 11:
            break

print(truncatables)
print(sum(truncatables))