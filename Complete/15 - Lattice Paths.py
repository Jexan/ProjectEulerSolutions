from math import factorial

def lattices(n):
	return(factorial(2*n)/(factorial(n)**2))

result = lattices(20)
if __name__ == '__main__':
    print(result)