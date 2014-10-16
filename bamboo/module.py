kTypeMethod = "kTypeMethod"
kTypeStruct = "kTypeStruct"

class Module:
	def __init__(self):
		self.classes = []

	def add_keyword(self, word):
		pass

	def num_classes(self):
		return len(self.classes)

	def get_class(self, num):
		return self.classes[num]