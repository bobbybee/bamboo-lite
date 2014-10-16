class DistributedParameter:
	def __init__(self, _type, name):
		self._type = _type
		self._name = name

	def name(self):
		return self._name

	def type(self):
		return self._type