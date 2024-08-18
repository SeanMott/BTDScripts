#gets the Open GL Math library

import GitOperations

#gets the include directory
GLM_INCLUDE_DIR = "Venders/GLM"

#clones GLM
def GetDep_GLM():
    GitOperations.GitClone("https://github.com/g-truc/glm.git", "GLM")