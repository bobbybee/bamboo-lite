kTypeMethod = "kTypeMethod"
kTypeStruct = "kTypeStruct"

class Module:
	def __init__(self):
		self.classes = []
		self.imports = []
		self.fields = []

	def add_keyword(self, word):
		pass

	def num_classes(self):
		return len(self.classes)

	def get_class(self, num):
		return self.classes[num]

	def num_imports(self):
		return len(self.imports)

	def get_import(self, n):
		return self.imports[n]

	def field_by_id(self, n):
		return self.fields[n]