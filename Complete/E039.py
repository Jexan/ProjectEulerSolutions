# Triangles with perimeter below 1000 with more solutions
# OPTIMAL (<0.05s)
# 
# APPROACH:
# 	Generate Pythagorean Triplets with perimeter under 1000.
# 	See 075.py's explanation to check a better theorical approach.
# 	
# NOTES:
# 	Using triplets reduced the runtime from 4 minutes to ~0.05 seconds (with unittest sometimes 0.00s 
# 	is reported as the runtime)
# 	The previous approach used sum(1..1000) iterations, with usage of floor and sqrts.
# 	The triplets approach instead used less than sum(1..10) iterations.

from .helpers import get_triangle_perimeters
LIMIT = 1001

DUMMY_PERIMETER = 120
DUMMY_RESULT = 3

def find_max_possible():
	val = max(counter)
	return counter.index(val)

counter = get_triangle_perimeters(LIMIT)

assert counter[DUMMY_PERIMETER] == DUMMY_RESULT
result = find_max_possible()