def adition(s, t):
	return (t[0]*s[1] + t[1]*s[0], s[1]*t[1])

def simplification(s, t):
	return (s[0]*t[1], s[1]*t[0])

def digit_sum(i):
	total = 0
	for y in str(i):
		total += int(y)

def create_terms(n):
	terms = []
	for i in range(1,n//3+2):
		terms.extend([(1,1),(2*i,1),(1,1)])

	return terms[:n+2]

terms = create_terms(98)
accumulated = terms.pop()
print(terms)

for i in terms[::-1]:
	accumulated = adition(simplification((1,1), accumulated), i)

n_term = adition((2,1), simplification((1,1), accumulated))

print(sum([int(i) for i in str(n_term[0])]))