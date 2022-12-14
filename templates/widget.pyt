from ikomia import core, dataprocess
from ikomia.utils import pyqtutils, qtconversion
from {{ PluginName }}.{{ PluginName }}_process import {{ PluginClassName }}Param
{{ QtImport }}


# --------------------
# - Class which implements widget associated with the process
# - Inherits PyCore.CWorkflowTaskWidget from Ikomia API
# --------------------
class {{ PluginClassName }}Widget({{ WidgetBaseClass }}):

    def __init__(self, param, parent):
        {{ WidgetBaseClass }}.__init__(self, parent)

        if param is None:
            self.parameters = {{ PluginClassName }}Param()
        else:
            self.parameters = param

        {{ QtLayout }}
        # Set widget layout
        self.setLayout(layout_ptr)

    def onApply(self):
        # Apply button clicked slot

        # Get parameters from widget
        # Example : self.parameters.windowSize = self.spinWindowSize.value()

        # Send signal to launch the process
        self.emitApply(self.parameters)


# --------------------
# - Factory class to build process widget object
# - Inherits PyDataProcess.CWidgetFactory from Ikomia API
# --------------------
class {{ PluginClassName }}WidgetFactory(dataprocess.CWidgetFactory):

    def __init__(self):
        dataprocess.CWidgetFactory.__init__(self)
        # Set the name of the process -> it must be the same as the one declared in the process factory class
        self.name = "{{ PluginName }}"

    def create(self, param):
        # Create widget object
        return {{ PluginClassName }}Widget(param, None)
