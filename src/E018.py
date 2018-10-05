# Get the biggest sum of the paths
# OPTIMAL (<0.3s)
# 
# Approach:
#   A brute force approach. Yield every sum, traversing all the tree with recurrence and
#   get the max sum.

nums = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

numbers = tuple(map(int, nums.split(' ')))
nodes = list()
rows = 15

def generate_tree():
    current_row = 0
    current_index = 0
    for row in range(rows):
        current_row += row

        for place in range(row+1):
            nodes.append(Node(numbers[current_row + place]))

def populate_nodes():
    current_row = 0
    current_index = 0

    for row in range(rows):
        current_row += row

        if row == rows - 1:
            break

        for place in range(row+1):
            target_node = nodes[current_row + place]
            target_left_index = current_row + place + row + 1

            target_node.left = nodes[target_left_index]
            target_node.right = nodes[target_left_index + 1]

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left  = left

generate_tree()
populate_nodes()

def generate_sums(node, total=0):
    if node is None:
        yield total
        return

    total += node.value

    for i in generate_sums(node.left, total):
        yield i
    for i in generate_sums(node.right, total):
        yield i

result = max(generate_sums(nodes[0]))
