class DCFile:
	def __init__(self, src):
		self.source = src
		self.parse()

	def parse(self):
		self.lines = self.source.split('\n')

		for ln in self.lines:
			print ln