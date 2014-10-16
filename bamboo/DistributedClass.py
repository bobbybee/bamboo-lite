class DistributedClass:
	def __init__(self, name):
		self._name = name
		self.fields = []

	def name(self):
		return self._name

	def num_fields(self):
		return len(self.fields)

	def get_field(self, num):
		return self.fields[num]