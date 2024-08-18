#handles generating build opiton flags in Premake

#generates a premake build option list
def GenerateBuildOptionFlagsString(flags):
    flagStr = "\n\nbuildoptions\n{\n"

    for d in flags:
        flagStr = flagStr + "\"" + d + "\",\n"

    flagStr = flagStr + "}\n"
    return flagStr