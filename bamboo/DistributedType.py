class DistributedType:
	def __init__(self, strType):
		self.strType = strType
		self.method = None

	def to_string(self):
		return self.strType

	def as_method(self):
		return self.method