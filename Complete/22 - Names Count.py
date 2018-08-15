file_dir = 'p022_names.txt'
f = open(file_dir, 'r')
acc = 0

content = f.read().replace('"', '').replace('\n', '').split(',')
content.sort()

def get_alpha_score(n):
	return sum([ord(i) - 64 for i in n])

assert(get_alpha_score('COLIN') == 53)
assert(content.index('COLIN') == 937)

for index, name in enumerate(content):
	acc += (index+1) * get_alpha_score(name)

print(acc)

f.close()