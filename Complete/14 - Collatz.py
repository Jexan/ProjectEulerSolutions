import operator as op
import functools as ft

limit = 1000000
collatz = {1:1}

def get_next_collatz(n):
	if n % 2 == 0:
		return n//2
	else:
		return n*3+1

for i in range(1, limit):
	n = i
	chain = 0
	if not i in collatz:
		to_add = []
		while True:
			chain += 1
			n = get_next_collatz(n)
			if n in collatz:
				chain += collatz[n]
				break
			else:
				to_add.append(n)
		collatz[i] = chain

		for y in to_add:
			chain -= 1
			collatz[y] = chain  	

keys = sorted(filter(ft.partial(op.gt, limit),collatz.keys()))
values = [collatz[i] for i in keys]

max_chain = max(values)
max_initial_val = values.index(max_chain) + 1

result = max_initial_val
if __name__ == '__main__':
	print(result)