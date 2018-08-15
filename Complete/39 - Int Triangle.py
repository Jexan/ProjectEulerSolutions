count = 1000
max_sol = 0
qtt_sol = 0

def find_possible(p):
	solutions = 0

	for i in range(1,p):
		i2 = i**2

		for j in range(i, p-i):
			j2 = j**2

			hyp = p - i - j

			if j2 + i2 == hyp**2:
				solutions += 1
				print(j, i, hyp) 

	return solutions

for i in range(1, count):
	c = find_possible(i)
	if c > qtt_sol:
		max_sol = i
		qtt_sol = c 

print(max_sol, qtt_sol)