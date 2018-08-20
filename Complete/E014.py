# Highest Collatz Chain under 1 million

DUMMY_N = 13
DUMMY_RESULT = 10

LIMIT = 1000000
collatz = {1:1}

def get_next_collatz(n):
	if n % 2 == 0:
		return n//2
	else:
		return n*3+1

def gen_collatz_chains(limit):
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

def get_max_chain():
	return max(collatz.items(), key=lambda x: x[1])[0]

gen_collatz_chains(LIMIT)

assert collatz[DUMMY_N] == DUMMY_RESULT
result = get_max_chain()