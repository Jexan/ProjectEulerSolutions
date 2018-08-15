nums = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
test = "3 7 4 2 4 6 8 5 9 3"

struct = []
counter = 1
numbers = list(map(int,test.split(' ')))
last_level = 4
sums = []

for i in range(last_level):
    struct.append(numbers[:counter])
    numbers = numbers[counter:]
    counter += 1

class Node(object):
    """docstring for Node"""
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left  = left

def left_value(head_level, index):
    if head_level != (last_level - 1):
        return Node(struct[head_level+1][index], left_value(head_level+1, index), right_value(head_level+1, index + 1))
    else:
        return Node(struct[head_level][index], None, None)

def right_value(head_level, index):
    if head_level != (last_level - 1):
        return Node(struct[head_level+1][index+1], left_value(head_level+1, index), right_value(head_level+1, index + 1))
    else:
        return Node(struct[head_level][index], None, None)

head = Node(struct[0][0], left_value(0,0), right_value(0,0))

