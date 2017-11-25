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

def makeFile(jsonObj, objname):
    declaration = "class "+objname+": Mappable {\n"
    
    properties = []

    for (key, value) in jsonObj.items():
        inferedType = inferType(value)

        if inferedType == 'Mappable':
            subMappable = value #json.load(value)
            makeFile(subMappable, key)
            inferedType = key
        
        sets = (key, inferedType)
        properties.append(sets)
    
    lines = []
    lines.append(declaration)

    # Var
    for (propName, dataType) in properties:
        s = "\tvar " + propName + ": " + dataType
        lines.append(s)
    
    # Init
    s = """
    init() {
    }

    required init?(map: Map) {
    }
    """
    lines.append(s)

    # Mapping
    s = "\tfunc mapping(map: Map) {"
    lines.append(s)

    for (propName, dataType) in properties:
        s = "\t\t" + propName + ' <- map["' + propName + '"]'
        lines.append(s)

    s = "\t}\n"
    lines.append(s)

    closing = "}"
    lines.append(closing)

    with open(objname+".swift", "w") as f:
        f.write("\n".join(lines))


json_object = json.loads(contents)
makeFile(json_object, "OutletProfile")


