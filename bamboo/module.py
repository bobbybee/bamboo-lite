class Module:
	def __init__(self):
		self.classes = []

	def add_keyword(self, word):
		print "Adding keyword "+word+"..."

	def num_classes(self):
		return len(self.classes)

	def get_class(self, num):
		return self.classes[num]