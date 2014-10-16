from DistributedType import DistributedType

class DistributedField:
	def __init__(self, name, paramList, modifierList):
		self._name = name
		self.paramList = paramList
		self.modifierList = modifierList

		self.type = DistributedType("kTypeMethod")
		self.type.method = self

	def name(self):
		return self._name

	def type(self):
		return self.type