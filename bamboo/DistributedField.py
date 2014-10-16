from DistributedType import DistributedType

class DistributedField:
	def __init__(self, name, paramList, modifierList):
		self._name = name
		self.paramList = paramList
		self.modifierList = modifierList

		self._type = DistributedType("kTypeMethod")
		self._type.method = self

	def name(self):
		return self._name

	def type(self):
		return self._type

	def num_parameters(self):
		return len(self.paramList)

	def get_parameter(self, p):
		return self.paramList[p]