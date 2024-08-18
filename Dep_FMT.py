#gets the FMT logging library

import GitOperations

#gets the include directory
FMT_INCLUDE_DIR = "Venders/FMT/include"

#clones FMT
def GetDep_FMT():
    GitOperations.GitClone("https://github.com/fmtlib/fmt.git", "FMT")