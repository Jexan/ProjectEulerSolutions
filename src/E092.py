# Find all numbers that get back to 1 when summing the digits
# TERRIBLY SLOW (Around 5 minutes)
#
# APPROACH:
# 	Brute force approach, including a lot of caching
# 	with digits sum and chain arriving.

LIMIT = 10000000

arrives_at_1 = {1:True, 89:False}
sum_of_digits = {str(i): i**2 for i in range(10)}
sum_of_digits[''] = 0

def get_digit_sum(n):
	str_num = str(n)

	last_digits = str_num[1:]
	last_sum = sum_of_digits.get(last_digits)

	if last_sum is None:
		last_sum = get_digit_sum(last_digits)
	
	sum_of_digit = sum_of_digits[str_num[0]] + last_sum
	sum_of_digits[sum_of_digit] = sum_of_digit
	
	return sum_of_digit

def n_numbers_who_arrive(limit): 
	for i in range(1, limit, -1):
		n = i
		if not n in arrives_at_1:
			to_add = []
			to_1 = False

			while True:
				n = get_digit_sum(n)
				if n in arrives_at_1:
					to_1 = arrives_at_1[n]
					break
				else:
					to_add.append(n)
			arrives_at_1[i] = to_1

			for y in to_add:
				arrives_at_1[y] = to_1  	

	numbers_who_arrive = filter(lambda x: not arrives_at_1[x], arrives_at_1.keys())
	return len(list(numbers_who_arrive))

result = n_numbers_who_arrive(LIMIT)