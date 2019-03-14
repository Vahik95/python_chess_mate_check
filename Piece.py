class Piece:
	piece_name = "empty"
	piece_color = ""

	def __init__(self, name=None, color=None):
		if (name and color) is not None:
			self.piece_name = name
			self.piece_color = color

