class GameSquare(object):
	def __init__(self, init_value: int, row: int, column: int):
		self.value = init_value
		self.row = row
		self.column = column

	def change_value(self, new_value: int) -> None:
		self.value = new_value
