class Point2d(object):
	"""store 1 point two dim """
	def __init__(self, x, y):
		self.x = x
		self.y = y

	"""return point do or don't equal Another point"""
	def Equals(self, pointOther):
		if self.x == pointOther.x and self.y == pointOther.y:
			return True
		else:
			return False
	"""return Decsition Up Dow Left Right from point to another point"""
	def Decisions(self, pointOther):
		if self.x == pointOther.x and self.y < pointOther.y:
			return "D"
		elif self.x == pointOther.x and self.y > pointOther.y:
			return "U"
		elif self.x > pointOther.x and self.y == pointOther.y:
			return "L"
		elif self.x < pointOther.x and self.y == pointOther.y:
			return "R"
		else:
			return "I don't know"