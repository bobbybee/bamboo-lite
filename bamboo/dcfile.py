import re
from DistributedClass import DistributedClass
from DistributedField import DistributedField
from DistributedParameter import DistributedParameter
from DistributedType import DistributedType

regexs = {
	"dclassDefinition": re.compile('dclass ([^ ]+) (: ([^ ]+) )?{'),
	"method": re.compile("\s+([^\(]+)\(([^\)]*)\)([^;]*);")
}

def parse_dcfile(mod, src):
	source = open(src, 'r').read()
	lines = source.split('\n')

	isInGroup = False
	groupName = ""
	isClass = False

	current = None

	for ln in lines:

		if not isInGroup:
			if regexs["dclassDefinition"].search(ln):
				mat = regexs["dclassDefinition"].match(ln)
				groupName = mat.group(1)

				# TODO: inheritance
				isInGroup = True
				isClass = True

				current = DistributedClass(groupName)

		else:
			if ln == "}":
				isInGroup = False

				if isClass:
					isClass = False
					mod.classes.append(current)

			elif regexs["method"].search(ln):
				mat = regexs["method"].match(ln)
				methodName = mat.group(1)
				parameterDump = mat.group(2)
				modifiersDump = mat.group(3)

				# extract parameters
				parameterList = []

				if len(parameterDump):
					parameters = parameterDump.split(',')

					for param in parameters:
						parts = param.strip().split(' ')

						name = None

						if len(parts) > 1 and not parts[-1].isdigit():
							name = parts[-1]
							parts = parts[:-1]

						t = " ".join(parts)

						parameterList.append(DistributedParameter(DistributedType(t), name))

				# extract modifiers
				modifierList = modifiersDump.split(' ')
				del modifierList[0] # fixes some bugs

				newField = DistributedField(methodName, parameterList, modifierList)
				current.fields.append(newField)