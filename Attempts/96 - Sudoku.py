from time import sleep
import pdb

class Sudoku():
	blank_dict = {i: True for i in range(1,10)}
	empty_squares = 0

	def __init__(self, board):
		self.set_board(board)
		self.populate()
		self.solve()

	def __repr__(self):
		string = '_' * 13 + '\n'
		for i, row in enumerate(self.board):
			string += '|'
			for j, item in enumerate(row):
				if isinstance(item, int):
					string += str(item)
				else:
					string += ' '

				if (j+1)%3 == 0:
					string += '|'

			string += '\n'

			if (i+1)%3 == 0:
				string += '_' * 13 + '\n'

		return string

	def set_board(self, board):
		self.board = []
		self.map = {}
		for i, row in enumerate(board):
			temp_row = []

			for j, item in enumerate(row):
				if item == 0:
					temp_row.append(self.blank_dict.copy())
					self.empty_squares += 1
				else:
					self.map[(i,j)] = item
					temp_row.append(item)

			self.board.append(temp_row)

	def done(self):
		#return self.empty_squares == 0
		return all(map(lambda x: isinstance(x, int), self.board[0][:3]))

	def digits(self):
		return int(''.join(map(str, self.board[0][:3])))

	def update_board(self, item, x, y):
		self.map[(y, x)] = item
		self.eliminate_row_and_col(item, x, y)
		self.eliminate_square(item, x, y)

	def eliminate_row_and_col(self, item, x, y):
		for i in range(9):
			row_item = self.board[y][i]
			col_item = self.board[i][x]

			if isinstance(row_item, dict):
				row_item[item] = False
			if isinstance(col_item, dict):
				col_item[item] = False

	def eliminate_square(self, item, x, y):
		sq_row = y//3
		sq_col = x//3
		for row in range(3):
			for col in range(3):
				place = self.board[sq_row*3+row][sq_col*3+col]
				if isinstance(place, dict):
						place[item] = False

	def populate(self):
		for y, x in self.map:
			item = self.board[y][x]
			self.eliminate_row_and_col(item, x, y)

		for col_square in range(3):
			for row_square in range(3):
				already_in = []
				square_map = {}
				
				for x in range(3):
					for y in range(3):
						i = col_square*3 + y
						j = row_square*3 + x
						item = self.board[i][j]

						if isinstance(item, int):
							already_in.append(item)
						else:
							square_map[(i,j)] = item

				for i in square_map.values():
					for j in already_in:
						i[j] = False

	def solve(self):
		while not self.done():
			for y, row in enumerate(self.board):
				for x, item in enumerate(row):
					if isinstance(item, dict):
						num_of_poss = 0
						possible_number = 0
						for number, poss in item.items():
							if poss: 
								num_of_poss += 1
								possible_number = number
						
						if num_of_poss == 1:
							self.empty_squares -= 1
							self.board[y][x] = possible_number
							self.update_board(possible_number, x, y)

			self.check_uniques()

	def check_uniques(self):
		print(self)
		sleep(.5)

		for y, row in enumerate(self.board):
			lacking_row = set()
			maps_row = {}
			
			lacking_col = set()
			maps_col = {}

			#Row Check
			for x, item in enumerate(row):
				if isinstance(item, dict):
					maps_row[(y,x)] = item
					for k, v in item.items():
						if not v:
							lacking_row.add(k)

				if isinstance(self.board[y][x], dict):
					maps_col[(y,x)] = self.board[y][x]
					for k, v in self.board[y][x].items():
						if not v:
							lacking_col.add(k)

			self.assure_uniques(maps_col, lacking_col)
			self.assure_uniques(maps_row, lacking_row)

		for col_square in range(3):
			for row_square in range(3):
				lacking_sq = set()
				maps_sq = {}
				
				for x in range(3):
					for y in range(3):
						i = col_square*3 + y
						j = row_square*3 + x

						if isinstance(self.board[j][i], dict):
							maps_sq[(j,i)] = self.board[j][i]
							for k, v in self.board[j][i].items():
								if not v:
									lacking_sq.add(k)

				self.assure_uniques(maps_sq, lacking_sq)

	def assure_uniques(self, maps, lacking):
		for i in lacking:
			possible = 0
			poss_coord = None

			for coord, poss in maps.items():
				if poss[i]:
					possible += 1
					poss_coord = coord
					if possible > 1:
						break

			if possible == 1:
				self.board[poss_coord[0]][poss_coord[1]] = i
				self.update_board(i, poss_coord[1], poss_coord[0])

sudokus = []
total = 0

with open('p096_sudoku.txt') as file:
	lins = file.readlines()

	for i in range(50):
		board = lins[(i*10+1):(i*10+10)]
		sudoku = []

		for j in board:
			sudoku.append([int(i) for i in j.replace("\n", '')])

		print(i)
		sudokus.append(Sudoku(sudoku))

for i in sudokus:
	total += sudokus.digits()

print(total)

# lins = """003020600
# 900305001
# 001806400
# 008102900
# 700000008
# 006708200
# 002609500
# 800203009
# 005010300"""

# sudoku = []

# for j in lins.splitlines():
# 	sudoku.append([int(i) for i in j])
# su = Sudoku(sudoku)

# print(su.board)
# print(su.digits())