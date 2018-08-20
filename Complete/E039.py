# Triangles with perimeter below 1000 with more solutions
# Very slow (4 minutes)

LIMIT = 1000

DUMMY_PERIMETER = 120
DUMMY_RESULT = 3

def find_possible(p):
	solutions = 0

	for i in range(1, p):
		i2 = i**2

		for j in range(i, p-i):
			j2 = j**2

			hyp = p - i - j

			if j2 + i2 == hyp**2:
				solutions += 1

	return solutions

def find_max_possible(limit):
	vals_gen = ((i, find_possible(i)) for i in range(1, limit))

	return max(vals_gen, key=lambda x: x[1])[0]

assert find_possible(DUMMY_PERIMETER) == DUMMY_RESULT
result = find_max_possible(LIMIT)