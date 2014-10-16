import re

regexs = {
	"dclassDefinition": re.compile('dclass ([^ ]+) (: ([^ ]+) )?{')
}

class DCFile:
	def __init__(self, src):
		self.source = src
		self.parse()

	def parse(self):
		self.lines = self.source.split('\n')

		isInGroup = False
		groupName = ""

		for ln in self.lines:
			print ln
			
			if not isInGroup:
				if regexs["dclassDefinition"].search(ln):
					mat = regexs["dclassDefinition"].match(ln)
					groupName = mat.group(1)

					# TODO: inheritance
					isInGroup = True

			else:
				if ln == "}":
					isInGroup = False

"""
getDCFileFromPath should not be used in production
this code stub is for testing bamboo lite in debug
"""

def getDCFileFromPath(path):
	file = open(path, 'r')
	return DCFile(file.read())

print getDCFileFromPath("sample.dc")
print regexs["dclassDefinition"]