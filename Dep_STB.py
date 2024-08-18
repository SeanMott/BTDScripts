#gets the STB header only library

import GitOperations

#gets the include directory
STB_INCLUDE_DIR = "Venders/STB"

#clones STB
def GetDep_STB():
    GitOperations.GitClone("https://github.com/nothings/stb.git", "STB")