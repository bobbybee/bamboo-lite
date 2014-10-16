import re
from DistributedClass import DistributedClass

regexs = {
	"dclassDefinition": re.compile('dclass ([^ ]+) (: ([^ ]+) )?{'),
	"method": re.compile("\s+([^\(]+)\(([^\)]+)\)([^;]*);")
}

def parse_dcfile(mod, src):
	source = open(src, 'r').read()
	lines = source.split('\n')

	isInGroup = False
	groupName = ""
	isClass = False

	for ln in lines:
		print ln
		
		if not isInGroup:
			if regexs["dclassDefinition"].search(ln):
				mat = regexs["dclassDefinition"].match(ln)
				groupName = mat.group(1)

				# TODO: inheritance
				isInGroup = True
				isClass = True

		else:
			if ln == "}":
				isInGroup = False

				if isClass:
					isClass = False

					t_cls = DistributedClass(groupName)
					mod.classes.append(t_cls)

			elif regexs["method"].search(ln):
				mat = regexs["method"].match(ln)
				methodName = mat.group(1)
				parameterDump = mat.group(2)
				modifiersDump = mat.group(3)

				print "Method Name: "+methodName
				print "parameterDump: "+parameterDump
				print "modifiersDump: "+modifiersDump