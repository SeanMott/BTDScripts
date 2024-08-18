#handles generating flags in Premake

#generates a premake flag list
def GenerateFlagsString(flags):
    flagStr = "\n\nflags\n{\n"

    for d in flags:
        flagStr = flagStr + "\"" + d + "\",\n"

    flagStr = flagStr + "}\n"
    return flagStr