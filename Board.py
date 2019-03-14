from Piece import *
import sys


class Board:
	mate = False
	chess_board = [[Piece()] * 8 for i in range(8)]

	letter_indexes = {
		'a': 0,
		'b': 1,
		'c': 2,
		'd': 3,
		'e': 4,
		'f': 5,
		'g': 6,
		'h': 7
	}

	def check_for_mate(self):
		if self.mate:
			print("\n There is a mate !!!")
			sys.exit()

	def print_board(self):
		print('\n'.join(['    '.join(['{:4}'.format(item.piece_name) for item in row]) for row in self.chess_board]))

	def letter_to_index(self, pos):
		if pos[0] in self.letter_indexes:
			return self.letter_indexes[pos[0]]

	def print_position(self, position):
		print(self.chess_board[position[0]][position[1]])

	def add_piece(self, name, color, position):
		if len(position) == 2 and name in ('king', 'queen', 'bishop', 'horse') and color in ('black', 'white'):
			if position[0] in 'abcdefgh' and position[1] in '123456789':
				self.chess_board[8 - int(position[1])][self.letter_indexes[position[0]]] = Piece(name, color)
		else:
			print("Wrong input !!!")

	def check_function(self, row, col):
		if self.chess_board[row][col].piece_name in self.piece_functions:
			self.piece_functions.get(self.chess_board[row][col].piece_name)(self, row, col)
			self.check_for_mate()

	def check_the_game(self):
		for i in range(8):
			for j in range(8):
				self.check_function(i, j)
		print("\nThere is no mate ")

	def find_routes(self, piece_name, row, col):
		routes = []
		d = {
			(row, col): self.chess_board[row][col] for row in range(len(self.chess_board)) for col in
			range(len(self.chess_board[0]))
		}
		if piece_name == 'king':
			routes = [
				(row + 1, col + 1), (row, col + 1), (row + 1, col),
				(row - 1, col + 1), (row - 1, col), (row, col - 1),
				(row + 1, col - 1), (row - 1, col - 1)
			]
		elif piece_name == 'horse':
			routes = [
				(row - 2, col + 1), (row - 1, col + 2), (row + 1, col + 2),
				(row + 2, col + 1), (row + 2, col - 1), (row + 1, col - 2),
				(row - 1, col - 2), (row - 2, col - 1)
			]

		elif piece_name == 'bishop':
			for i in range(1, 8 - col + 1):
				if d.get((row - i, col + i)) is not None:
					if d.get((row - i, col + i)).piece_name in ('empty', 'king'):
						routes.append((row - i, col + i))
					else:
						break

			for i in range(1, 8 - col + 1):
				if d.get((row + i, col + i)) is not None:
					if d.get((row + i, col + i)).piece_name in ('empty', 'king'):
						routes.append((row + i, col + i))
					else:
						break

			for i in range(1, col + 1):
				if d.get((row - i, col - i)) is not None:
					if d.get((row - i, col - i)).piece_name in ('empty', 'king'):
						routes.append((row - i, col - i))
					else:
						break

			for i in range(1, col + 1):
				if d.get((row + i, col - i)) is not None:
					if d.get((row + i, col - i)).piece_name in ('empty', 'king'):
						routes.append((row + i, col - i))
					else:
						break

		elif piece_name == 'queen':
			for i in range(1, row + 1):
				if d.get((row - i, col)) is not None:
					if d.get((row - i, col)).piece_name in ('empty', 'king'):
						routes.append((row - i, col))
					else:
						break

			for i in range(1, 8 - row + 1):
				if d.get((row + i, col)) is not None:
					if d.get((row + i, col)).piece_name in ('empty', 'king'):
						routes.append((row + i, col))
					else:
						break

			for i in range(1, col + 1):
				if d.get((row, col - i)) is not None:
					if d.get((row, col - i)).piece_name in ('empty', 'king'):
						routes.append((row, col - i))
					else:
						break

			for i in range(1, 8 - col + 1):
				if d.get((row, col + i)) is not None:
					if d.get((row, col + i)).piece_name in ('empty', 'king'):
						routes.append((row, col + i))
					else:
						break

		result = filter(None, [d.get(i) for i in routes])

		return result

	def king_function(self, row, col):
		for x in self.find_routes('king', row, col):
			if x.piece_color != self.chess_board[row][col].piece_color and x.piece_name == 'king':
				self.mate = True

	def horse_function(self, row, col):
		for x in self.find_routes('horse', row, col):
			if x.piece_color != self.chess_board[row][col].piece_color and x.piece_name == 'king':
				self.mate = True

	def bishop_function(self, row, col):
		for x in self.find_routes('bishop', row, col):
			if x.piece_color != self.chess_board[row][col].piece_color and x.piece_name == 'king':
				self.mate = True

	def queen_function(self, row, col):
		for x in self.find_routes('bishop', row, col):
			if x.piece_color != self.chess_board[row][col].piece_color and x.piece_name == 'king':
				self.mate = True
		for x in self.find_routes('queen', row, col):
			if x.piece_color != self.chess_board[row][col].piece_color and x.piece_name == 'king':
				self.mate = True

	piece_functions = {
		'king': king_function,
		'horse': horse_function,
		'bishop': bishop_function,
		'queen': queen_function
	}
