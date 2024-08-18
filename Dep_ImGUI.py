#gets ImGUI

import GitOperations

#gets the include directory
IMGUI_INCLUDE_DIR = "Venders/ImGUI"

#gets the source paths
IMGUI_SRC_FILES = """---imgui
    "Venders/ImGUI/imconfig.h",
	"Venders/ImGUI/imgui.h",
	"Venders/ImGUI/imgui.cpp",
	"Venders/ImGUI/imgui_draw.cpp",
	"Venders/ImGUI/imgui_internal.h",
	"Venders/ImGUI/imgui_tables.cpp",
	"Venders/ImGUI/imgui_widgets.cpp",
	"Venders/ImGUI/imstb_rectpack.h",
	"Venders/ImGUI/imstb_textedit.h",
	"Venders/ImGUI/imstb_truetype.h",
	"Venders/ImGUI/imgui_demo.cpp",
    
    "Venders/ImGUI/backends/imgui_impl_sdl2.cpp",
    "Venders/ImGUI/backends/imgui_impl_vulkan.cpp",\n\n"""

#clones ImGUI
def GetDep_ImGUI():
    GitOperations.GitClone("https://github.com/ocornut/imgui.git", "ImGUI")