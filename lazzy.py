import json

print("Lazzy version 1.0")

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

    raise ValueError('Unable to infer a value.')

def process(jsonObj):
    properties = []

    for (key, value) in jsonObj.items():
        inferedType = inferType(value)

        if inferedType == 'Mappable':
            subMappable = value #json.load(value)
            makeFile(subMappable, key)
            inferedType = key
        
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


def makeFile(jsonObj, objname):
    lines = []
    properties = process(jsonObj)

    start = "class "+objname+": Mappable {\n"

    declarations = generateDeclarations(properties)
    initBlock = generateInitBlock()
    mappingBlock = generateMappingBlock(properties)

    end = "}"

    lines.append(start)
    lines.extend(declarations)
    lines.append(initBlock)
    lines.extend(mappingBlock)
    lines.append(end)

    with open(objname+".swift", "w") as f:
        f.write("\n".join(lines))


json_object = json.loads(contents)
makeFile(json_object, "OutletProfile")


