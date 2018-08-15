from math import factorial

factorials = [factorial(i) for i in range(10)]

def digit_factorials_sum(n):
	return sum(factorials[int(i)] for i in str(n))

digits = []

assert(digit_factorials_sum(145) == 145)

for i in range(2500000):
	if digit_factorials_sum(i) == i:
		digits.append(i)

result = sum(digits)
if __name__ == '__main__':
    print(result)