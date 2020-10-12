from game_board import GameBoard
from four_colors_game import FourColorsGame
from game_ui_manager import GameUIManager


class FourColorsGameBuilder(object):
	def __init__(self, board_size: int, number_of_turns: int, number_of_values: int, colors: list):
		self.board_size = board_size
		self.number_of_turns = number_of_turns
		self.number_of_values = number_of_values
		self.colors = colors

	def build(self) -> FourColorsGame:
		board = GameBoard(self.board_size, self.board_size, self.number_of_values)
		ui_manager = GameUIManager(self.colors)
		return FourColorsGame(board, ui_manager, self.number_of_turns)
