import json

print("Lazzy version 1.0")
print("just refactor -> rename the classes with bad names")

fname = "target.json"
rname = "result.swift"

with open(fname, "r") as file:
    contents = file.read()

def inferType(value):
    infer = type(value)
    inferedType = ""
    if infer == bool:
        return "Bool"
    if infer == unicode:
        return "String"
    if infer == int:
        return "Int"
    if infer == float:
        return "Double"
    if infer == dict:
        return "Mappable"

    isList = isinstance(value, list)

    if isList:
        if not value:
            return "[<#Unknown#>]"
        else:
            inferred = inferType(value[0])
            if inferType(value[0]) == "Mappable":
                return "Mappable Array"
            return "[{}]".format(inferred)

    raise ValueError('Unable to infer a value.')

def process(jsonObj):
    properties = []

    for (key, value) in jsonObj.items():
        inferedType = inferType(value)

        if inferedType == 'Mappable':
            subMappable = value #json.load(value)
            inferedType = key+"Object"
            makeFile(subMappable, inferedType)

        if inferedType == 'Mappable Array':
            subMappable = value[0]
            objectName = "{}Object".format(key)
            inferedType = "[{}]".format(objectName)
            makeFile(subMappable, objectName)
        
        sets = (key, inferedType)
        properties.append(sets)

    return properties
        
def generateDeclarations(properties):
    declarations = []
    for (propName, dataType) in properties:
        s = "var " + propName + ": " + dataType
        declarations.append(s)
    return declarations

def generateInitBlock():
    return """
    init() {
    }

    required init?(map: Map) {
    }
    """

def generateMappingBlock(properties):
    mappingBlock = []
    mappingBlock.append("func mapping(map: Map) {")
    for (propName, dataType) in properties:
        s = propName + ' <- map["' + propName + '"]'
        mappingBlock.append(s)
    mappingBlock.append("}")
    return mappingBlock


def indent(lines):
    indention_level = 0
    indented_lines = []
    for line in lines:
        if line == "}":
            indention_level -= 1

        indent = "\t" * indention_level
        indented_lines.append(indent+line)
        
        if line.endswith("{"):
            indention_level += 1

    return indented_lines

def makeFile(jsonObj, objname):
    lines = []
    properties = process(jsonObj)

    start = "class "+objname+": Mappable {"

    declarations = generateDeclarations(properties)
    initBlock = generateInitBlock()
    mappingBlock = generateMappingBlock(properties)

    end = "}"

    lines.append(start)
    lines.extend(declarations)
    lines.append(initBlock)
    lines.extend(mappingBlock)
    lines.append(end)

    indented_lines = indent(lines)

    with open(objname+".swift", "w") as f:
        f.write("\n".join(indented_lines))


json_object = json.loads(contents)
makeFile(json_object, "<#ModelName#>")


