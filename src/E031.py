# In how many ways can 2 pounds be written
# OPTIMAL (<0.1s)
# 
# APPROACH:
# 	Use recursion and function cache to reduce the 
# 	200 pences to 0.
# 	
# NOTES:
# 	Without cache, the problem takes 20 seconds.
# 	With bounded (32) cache, the problem takes 2 seconds.

from itertools import takewhile
from functools import lru_cache

possible = (1, 2, 5, 10, 20, 50, 100, 200)

@lru_cache(None)
def redux(n, m):
	if not n:
		return 1
	
	total = 0
	for i in takewhile(lambda x: x<=n and x<=m, possible):
		total += redux(n-i, i)
	return total

result = redux(200, 200)