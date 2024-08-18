#generates Premake files

#generates Workspace
def GenerateWorkspace(solutionName, arch, startUpProject = None):
    work = "workspace \"" + solutionName + "\"\narchitecture \"" + arch + "\"\n"

    if startUpProject is not None:
        work = work + "startproject \"" + startUpProject + "\""
    
    return work

#generates default configurations
def GenerateDefaultConfigureations():
    return """

configurations
{
    "Debug",
    "Release",
    "Dist"
}


"""

#generates default binary output path
def GenerateDefaultBinaryOutputPath():
    return "bin/%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

#defines the project settings for a configuration
class ConfigurationSettings:

    #init
    def __init__(self):
        self.optimize = "On"

        self.defines = {}
        self.flags = {}
        self.links = {}

#defines the project settings for a platform
class PlatformSettings:

    #init
    def __init__(self):
        self.cppdialect = "C++20"
        self.staticruntime = "On"
        self.systemversion = "latest"

        self.defines = {}

#defines a project
class Project:

    #init
    def __init__(self):
        self.name = "PremakeProject"
        self.kind = "ConsoleApp"
        self.language = "C++"
        
        self.location = None
        self.desc = None

        self.binaryOutput = GenerateDefaultBinaryOutputPath()

        #global settings
        self.sourceFiles = []
        self.includeDirs = []
        self.links = {}

        self.defines = {}

        self.flags = {}

        self.buildOptions = {}

        #platform settings
        self.windowsSettings = PlatformSettings() #windows desktop settings
        self.macMSettings = PlatformSettings() #Mac M Series desktop settings
        self.macIntelSettings = PlatformSettings() #Mac Intel desktop settings
        self.LinuxSettings = PlatformSettings() #Linux desktop settings

        #configure settings
        self.debugCongfigSettings = ConfigurationSettings()
        self.releaseCongfigSettings = ConfigurationSettings()
        self.distCongfigSettings = ConfigurationSettings()
    
    #generates a project header string
    def GenerateProjectHeaderString(self):
        project = ""
    
        if self.desc is not None:
            project = project + "---" + self.desc + "\n"

        project = project + "project \"" + self.name + "\"\n"

        if self.location is not None:
            project = project + "location \"" + self.location + "\"\n"

        project = project + "kind \"" + self.kind + "\"\n"

        project = project + "language \"" + self.language + "\"\n"

        project = project + "targetdir (\"" + self.binaryOutput + "\")\n"
        project = project + "objdir (\"" + self.binaryOutput + "\")\n"

        return project
    

    #generates a source files string
    def GenerateProjectSourceString(self):
        project = """\n\nfiles 
{
---base code
"""
        loc = ""
        if self.location is not None:
            loc = self.location
        project = project + "\"" + loc + "/includes/**.h\",\n"
        project = project + "\"" + loc + "/src/**.c\",\n"
        project = project + "\"" + loc + "/includes/**.hpp\",\n"
        project = project + "\"" + loc + "/src/**.cpp\",\n\n"

        #include extra source files
        for s in self.sourceFiles:
            project = project + "\"" + s + "\",\n"

        project = project + """}"""

        return project

    #generates a includes string
    def GenerateProjectIncludeString(self):
        project = """\n\nincludedirs 
{
---base code
"""
        loc = ""
        if self.location is not None:
            loc = self.location
        project = project + "\"" + loc + "/includes\",\n"

        #include extra includes files
        for s in self.includeDirs:
            project = project + "\"" + s + "\",\n"

        project = project + """}"""

        return project