acc = 0
square_side = 5

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
	
result = sum([i for i in generate_numbers(square_side)])
if __name__ == '__main__':
    print(result)