#handles generating links in Premake

#generates a premake link list
def GenerateLinksString(links):
    linkStr = "\n\nlinks\n{\n"

    for d in links:
        linkStr = linkStr + "\"" + d + "\",\n"

    linkStr = linkStr + "}\n"
    return linkStr