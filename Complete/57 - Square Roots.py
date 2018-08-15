def adition(s, t):
	return (t[0]*s[1] + t[1]*s[0], s[1]*t[1])

def is_criterion(s):
	return (len(str(s[0])) > len(str(s[1])))

def simplification(s, t):
	return (s[0]*t[1], s[1]*t[0])

sums = [(1,2)]
total = 0

for i in range(999):
	denominator = adition((2,1), sums[i])

	sums.append(simplification((1,1), denominator))

for i in sums:
	if is_criterion(adition(i, (1,1))):
		total += 1

print(total)