#gets Vulkan libraries

import GitOperations

#gets the include directory
VMA_INCLUDE_DIR = "Venders/VMA/include"

#gets the include directory
VK_BOOTSTRAP_INCLUDE_DIR = "Venders/VKBootstrap/src"

#lists all the files we need to include
VK_BOOTSTRAP_SOURCE_FILE_NAMES = [
	"VkBootstrap.cpp",
	"VkBootstrap.h",
	"VkBootstrapDispatch.h"
]

#adds the source paths to the source list in a Premake project
def AddSources_VkBootstrap(srcs):
	for f in VK_BOOTSTRAP_SOURCE_FILE_NAMES:
		srcs.append(VK_BOOTSTRAP_INCLUDE_DIR + "/" + f)

#the path to the vulkan include
VULKAN_INCLUDE_DIR = "C:/VulkanSDK/1.3.283.0/Include"

#the link path for the vulkan
VULKAN_LINK_DIR = "C:/VulkanSDK/1.3.283.0/Lib/vulkan-1.lib"

#clones Vulkan libraries
def GetDep_VulkanLibraries():
    GitOperations.GitClone("https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git", "VMA")
    GitOperations.GitClone("https://github.com/charles-lunarg/vk-bootstrap.git", "VKBootstrap", "main")