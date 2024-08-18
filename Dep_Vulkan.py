#gets Vulkan libraries

import GitOperations

#gets the include directory
VMA_INCLUDE_DIR = "Venders/VMA/include"

#gets the include directory
VK_BOOTSTRAP_INCLUDE_DIR = "Venders/VKBootstrap/src"

#the path to the vulkan include
VULKAN_INCLUDE_DIR = "C:/VulkanSDK/1.3.283.0/Include"

#gets the source files
VK_BOOTSTRAP_SRC_DIR = """---vulkan bootstrapper
    "Venders/VKBootstrap/src/**.cpp",
    "Venders/VKBootstrap/src/**.h",\n\n"""

#the link path for the vulkan
VULKAN_LINK_DIR = "C:/VulkanSDK/1.3.283.0/Lib/vulkan-1.lib"

#clones Vulkan libraries
def GetDep_VulkanLibraries():
    GitOperations.GitClone("https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git", "VMA")
    GitOperations.GitClone("https://github.com/charles-lunarg/vk-bootstrap.git", "VKBootstrap", "main")