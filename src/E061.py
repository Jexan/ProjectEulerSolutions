# Get the only six 4 digits numbers that fullfil the conditions.
# OPTIMAL (<0.05s)
#
# APPROACH:
#   Get the beginings (sp?) for all the possible four digits geometric numbers,
#   then, starting with triangular numbers, check if there's any other geometric number
#   that starts with that number two last digits (they're checked in the calculated beginings).
#   
#   Checking off every possibility, we yield just the combination of 6 numbers, which is known to be unique.

from collections import defaultdict

triangles = tuple(n*(n+1)//2 for n in range(45, 141))
squares = tuple(n**2 for n in range(32, 100))
pentagonal = tuple(n*(3*n-1)//2 for n in range(26, 82))
hexagonal = tuple(n*(2*n-1) for n in range(23, 71))
heptagonal = tuple(n*(5*n-3)//2 for n in range(21, 64))
octagonal = tuple(n*(3*n-2) for n in range(19, 59))

order = (squares, pentagonal, hexagonal, heptagonal, octagonal)

def get_beginings(iterator, end=False):
    ends = defaultdict(list)

    for number in iterator:
        if end:
            index_2 = str(number)[2:]
        else:
            index_2 = str(number)[:2] 

        ends[index_2].append(number)

    return ends

beginings = list(get_beginings(ns) for ns in order)
def check_criteria(v, carries=(), nums=()):
    if len(nums) == 6:
        if str(v)[2:] == str(nums[0])[:2]:
            yield sum(nums)
        return
    if not nums:
        nums = (v,)

    two_last_key = str(v)[2:]
    for beggining_dict in beginings:
        if beggining_dict in carries:
            continue

        for i in beggining_dict.get(two_last_key, ()):
            for k in check_criteria(i, (*carries, beggining_dict), (*nums, i)): yield k

    return

def get_result():
    for i in triangles:
        for result in check_criteria(i):
            return result

result = get_result()
