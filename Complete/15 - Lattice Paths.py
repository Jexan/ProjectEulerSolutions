from math import factorial

def lattices(n):
	return(factorial(2*n)/(factorial(n)**2))

print(lattices(20))