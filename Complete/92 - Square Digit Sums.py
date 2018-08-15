import operator as op
import functools as ft

limit = 10000000
arrives_at_1 = {1:True, 89:False}

def get_digit_sum(n):
	return sum([int(i)**2 for i in str(n)])

assert(get_digit_sum(44) == 32)

for i in range(1, limit):
	n = i
	if not i in arrives_at_1:
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

keys = sorted(filter(ft.partial(op.gt, limit),arrives_at_1.keys()))
values = [arrives_at_1[i] for i in keys if not arrives_at_1[i]]

assert(not arrives_at_1[42])

print(len(values))