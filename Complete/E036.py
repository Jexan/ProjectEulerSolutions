# Sum of palindromes under 1.000.000 that are also palindrome in binary.
# OPTIMAL (<0.1s)
#  
# APPROACH:
#   The palindromes under one million are smartly generated, only having to test against
#   1999 numbers if their binary repr is palindrome.

def bin_is_palindrome(n):
    bin_n = bin(n)[2:]

    return bin_n == bin_n[::-1]

def generate_palindromes():
    for i in range(1, 10):
        yield i

    for i in range(1, 100):
        str_i = str(i)
        reverse_i = str_i[::-1]

        yield int(str_i + reverse_i)

        for j in range(0, 10):
            yield int(str_i + str(j) + reverse_i)

    for i in range(100, 1000):
        str_i = str(i)
        yield int(str_i + str_i[::-1])
         

result = sum(filter(bin_is_palindrome, generate_palindromes()))