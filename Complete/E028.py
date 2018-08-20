# Sum of the diagonals of a spiral square diagonal

SQUARE_SIDE = 1001
DUMMY_SQUARE_SIDE = 5
DUMMY_RESULT = 101

def generate_numbers(limit):
	current = 1
	internal_square = 1
	steps = 0
	while internal_square <= limit:
		yield current
		if current == internal_square**2:
			internal_square += 2
			steps += 2

		current += steps

def sum_diagonals(square_side):
	return sum(generate_numbers(square_side))
	
assert sum_diagonals(DUMMY_SQUARE_SIDE) == DUMMY_RESULT
result = sum_diagonals(SQUARE_SIDE)