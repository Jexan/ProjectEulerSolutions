def pentagonal(n):
	return n*(3*n-1)/2

def hexagonal(n):
	return n*(2*n-1)

def triangular(n):
	return n*(n+1)/2

pent, tri, hexa = set(), set(), set()
n = 1
common = None

while True:
	for i in range(n, n+10000):
		pent.add(pentagonal(i))
		tri.add(triangular(i))
		hexa.add(hexagonal(i))

	common = pent.intersection(tri.intersection(hexa))

	if len(common) > 2: break

	n += 10000

result = common
if __name__ == '__main__':
    print(result)