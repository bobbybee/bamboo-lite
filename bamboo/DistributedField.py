class DistributedField:
	def __init__(self, name, paramList, modifierList):
		self._name = name
		self.paramList = paramList
		self.modifierList = modifierList

		print self.paramList
		print self.modifierList

	def name(self):
		return self._name