from game_square import GameSquare
from random import randint


class GameBoard(object):
	def __init__(self, rows: int, columns: int, number_of_values: int):
		self.board = []
		for i in range(rows):
			self.board.append([])
			for j in range(columns):
				self.board[i].append(GameSquare(randint(0, number_of_values - 1), i, j))

	def get_right_neighbours(self, square: GameSquare) -> list:
		row = square.row
		column = square.column
		neighbours = []
		if row < len(self.board) - 1:
			neighbours.append(self.board[row + 1][column])
			if column < len(self.board[0]) - 1:
				neighbours.append(self.board[row + 1][column + 1])

		if column < len(self.board[0]) - 1:
			neighbours.append(self.board[row][column + 1])

		return neighbours

	def get_square(self, row, column) -> GameSquare:
		if row < len(self.board) and column < len(self.board[0]):
			return self.board[row][column]
		return None

	def is_all_board_with_same_value(self) -> bool:
		value = self.get_square(0, 0).value
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j].value != value:
					return False
		return True
