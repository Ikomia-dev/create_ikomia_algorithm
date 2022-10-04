from ikomia import dataprocess


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits PyDataProcess.CPluginProcessInterface from Ikomia API
# --------------------
class IkomiaPlugin(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        from {{ PluginName }}.{{ PluginName }}_process import {{ PluginClassName }}Factory
        return {{ PluginClassName }}Factory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        from {{ PluginName }}.{{ PluginName }}_widget import {{ PluginClassName }}WidgetFactory
        return {{ PluginClassName }}WidgetFactory()
