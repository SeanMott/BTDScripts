#gets the SDL library

import GitOperations
import os
import subprocess
import shutil

#gets the include directory
SDL_INCLUDE_DIR = "Venders/SDL/include"

#gets the debug link lib for SDL
SDL_VERSION_DEBUG_LINK_FILEPATH = "Venders/SDL/Build/RelWithDebInfo/SDL2.lib"

#gets the release link lib for SDL
SDL_VERSION_RELEASE_LINK_FILEPATH = "Venders/SDL/Build/Release/SDL2.lib"

#gets the distribution link lib for SDL
SDL_VERSION_DIST_LINK_FILEPATH = "Venders/SDL/Build/MinSizeRel/SDL2.lib"

#clones SDL
def GetDep_SDL():
    GitOperations.GitClone("https://github.com/libsdl-org/SDL.git", "SDL", "SDL2")

#builds SDL
def Build_SDL():
    #checks if Vender folder exists
    if not os.path.exists("Venders"):
        print("SDL HAS TO BE DOWNLOADED FIRST USING \"GetDep_SDL\" BEFORE IT CAN BE BUILT")
        return
    
    #checks if Vender/DLL folder exists
    if not os.path.exists("Venders/Build"):
        os.mkdir("Venders/Build")
        os.mkdir("Venders/Build/Debug")
        os.mkdir("Venders/Build/Release")
        os.mkdir("Venders/Build/Dist")
    
    #builds each of the SDL configs
    #subprocess.run(["cmake", "-S", "Venders/SDL", "-B", "Venders/SDL/Build"],
     #   shell=True)
    #subprocess.run(["msbuild", "Venders/SDL/Build/SDL2.sln", "-maxCpuCount:4", "/property:Configuration=Release"],
    #    shell=True)
    #subprocess.run(["msbuild", "Venders/SDL/Build/SDL2.sln", "-maxCpuCount:4", "/property:Configuration=MinSizeRel"],
    #    shell=True)
    #subprocess.run(["msbuild", "Venders/SDL/Build/SDL2.sln", "-maxCpuCount:4", "/property:Configuration=RelWithDebInfo"],
    #    shell=True)

    #copy to the Vender/Build folder for each config
    shutil.copyfile("Venders/SDL/Build/RelWithDebInfo/SDL2.dll", "Venders/Build/Debug/SDL2.dll")
    shutil.copyfile("Venders/SDL/Build/Release/SDL2.dll", "Venders/Build/Release/SDL2.dll")
    shutil.copyfile("Venders/SDL/Build/MinSizeRel/SDL2.dll", "Venders/Build/Dist/SDL2.dll")