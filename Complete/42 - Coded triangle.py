from math import floor

file_dir = 'p042_words.txt'
triangular_words = 0

f = open(file_dir, 'r')
content = f.read().replace('"', '').replace('\n', '').split(',')

def get_alpha_score(n):
	return sum([ord(i) - 64 for i in n])

def triangular(n):
	return floor(n*(n+1)/2)


tri_ns = [triangular(i) for i in range(35)]
assert(get_alpha_score('SKY') in tri_ns)

for i in content:
	if get_alpha_score(i) in tri_ns:
		triangular_words += 1


result = triangular_words
if __name__ == '__main__':
    print(result)

f.close()