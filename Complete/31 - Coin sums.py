from itertools import takewhile
from operator  import le
from functools import partial 

poss = 0
possible = [1,2,5,10,20,50,100,200]
quantity = {}

def cut(n,m):
	comp_max = partial(ge, n)
	comp_less = partial(ge, m)
	return takewhile(comp_less, takewhile(comp_max, possible))

def redux(n, m):
	if n==0:
		global poss
		poss += 1  
		return
	for i in cut(n, m):
		redux(n-i, i)

redux(200, 200)

result = poss
if __name__ == '__main__':
    print(result)