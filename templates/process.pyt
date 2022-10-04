import copy
from ikomia import core, dataprocess


# --------------------
# - Class to handle the process parameters
# - Inherits core.CWorkflowTaskParam from Ikomia API
# --------------------
class {{ PluginClassName }}Param(core.CWorkflowTaskParam):

    def __init__(self):
        core.CWorkflowTaskParam.__init__(self)
        # Place default value initialization here
        # Example : self.windowSize = 25

    def setParamMap(self, param_map):
        # Set parameters values from Ikomia application
        # Parameters values are stored as string and accessible like a python dict
        # Example : self.windowSize = int(param_map["windowSize"])
        pass

    def getParamMap(self):
        # Send parameters values to Ikomia application
        # Create the specific dict structure (string container)
        param_map = core.ParamMap()
        # Example : paramMap["windowSize"] = str(self.windowSize)
        return param_map


# --------------------
# - Class which implements the process
# - Inherits core.CWorkflowTask or derived from Ikomia API
# --------------------
class {{ PluginClassName }}({{ ProcessBaseClass }}):

    def __init__(self, name, param):
        {{ ProcessBaseClass }}.__init__(self, name)
        # Add input/output of the process here
        # Example :  self.addInput(dataprocess.CImageIO())
        #           self.addOutput(dataprocess.CImageIO())

        # Create parameters class
        if param is None:
            self.setParam({{ PluginClassName }}Param())
        else:
            self.setParam(copy.deepcopy(param))

    def getProgressSteps(self):
        # Function returning the number of progress steps for this process
        # This is handled by the main progress bar of Ikomia application
        return 1

    def run(self):
        # Core function of your process
        # Call beginTaskRun for initialization
        self.beginTaskRun()

        # Examples :
        # Get input :
        # input = self.getInput(indexOfInput)

        # Get output :
        # output = self.getOutput(indexOfOutput)

        # Get parameters :
        # param = self.getParam()

        # Get image from input/output (numpy array):
        # srcImage = input.getImage()

        # Call to the process main routine
        # dstImage = ...

        # Set image of input/output (numpy array):
        # output.setImage(dstImage)

        # Step progress bar:
        self.emitStepProgress()

        # Call endTaskRun to finalize process
        self.endTaskRun()


# --------------------
# - Factory class to build process object
# - Inherits dataprocess.CTaskFactory from Ikomia API
# --------------------
class {{ PluginClassName }}Factory(dataprocess.CTaskFactory):

    def __init__(self):
        dataprocess.CTaskFactory.__init__(self)
        # Set process information as string here
        self.info.name = "{{ PluginName }}"
        self.info.shortDescription = "your short description"
        self.info.description = "your description"
        # relative path -> as displayed in Ikomia Studio process tree
        self.info.path = "Plugins/Python"
        self.info.version = "1.0.0"
        # self.info.iconPath = "your path to a specific icon"
        self.info.authors = "algorithm author"
        self.info.article = "title of associated research article"
        self.info.journal = "publication journal"
        self.info.year = 2022
        self.info.license = "MIT License"
        # URL of documentation
        self.info.documentationLink = ""
        # Code source repository
        self.info.repository = ""
        # Keywords used for search
        self.info.keywords = "your,keywords,here"

    def create(self, param=None):
        # Create process object
        return {{ PluginClassName }}(self.info.name, param)
