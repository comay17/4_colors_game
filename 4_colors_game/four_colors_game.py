from game_board import GameBoard
from game_square import GameSquare
from game_ui_manager import GameUIManager


class FourColorsGame(object):
	def __init__(self, board: GameBoard, ui_manager: GameUIManager, number_of_turns: int):
		self.board = board
		self.ui_manager = ui_manager
		self.number_of_turns = number_of_turns
		self.is_winner = False

	def run(self) -> None:
		turn = 1
		while turn <= self.number_of_turns and not self.is_winner:
			self.run_turn(turn)
			turn += 1
		self.ui_manager.print_board(self.board)
		if self.is_winner:
			print("You won!")
		else:
			print ("You lost!")

	def run_turn(self, turn: int):
		self.ui_manager.print_board(self.board)
		color_input = self._get_user_input_for_turn(turn)
		if not self.ui_manager.validate_input_color(color_input):
			raise Exception('input is not valid')
		input_value = self.ui_manager.get_input_value(color_input)
		self._update_values_for_turn(input_value)
		self._update_is_winner()

	def _update_is_winner(self):
		self.is_winner = self.board.is_all_board_with_same_value()

	def _get_user_input_for_turn(self, turn: int) -> str:
		input_color = input("Turn {}, choose color: ".format(turn))
		return input_color

	def _update_values_for_turn(self, new_value: int):
		start_square = self.board.get_square(0, 0)
		squares_to_update = set()
		self._get_squares_to_update(start_square, start_square.value, squares_to_update)
		for square in squares_to_update:
			square.change_value(new_value)

	def _get_squares_to_update(self, square: GameSquare, value: int, squares_to_update: set) -> list:
		if square in squares_to_update:
			return
		if square.value == value:
			squares_to_update.add(square)
			neighbours = self.board.get_right_neighbours(square)
			for neighbour in neighbours:
				self._get_squares_to_update(neighbour, value, squares_to_update)
