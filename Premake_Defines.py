#handles generating define strings for Premake projects

#generates a premake define list
def GenerateDefinesString(defines):
    defineStr = "\n\ndefines\n{\n"

    for d in defines:
        defineStr = defineStr + "\"" + d + "\",\n"

    defineStr = defineStr + "}\n"
    return defineStr