from termcolor import cprint
from game_board import GameBoard

SQUARE_TEXT_VALUE = '   '


class GameUIManager(object):
	def __init__(self, colors: list):
		self.colors = colors

	def validate_input_color(self, color_input: str) -> bool:
		return any([color for color in self.colors if color.startswith(color_input)])

	def get_input_value(self, color_input: str) -> int:
		# if have time will add validation that colors don't start in the same letter
		# if will have time will raise an exception if none found
		for color in self.colors:
			if color.startswith(color_input):
				return self.colors.index(color)
		return 0

	def _print_square(self, square):
		color = self.colors[square.value]
		cprint(SQUARE_TEXT_VALUE, color, "on_{}".format(color), end='')

	def _print_row(self, row):
		for square in row:
			self._print_square(square)
		print()

	def print_board(self, board: GameBoard):
		for row in board.board:
			self._print_row(row)
