import ctypes

class VkDisplayModePropertiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDisplayModeParametersKHR',
    }
    _included_in_ = {
        'VkDisplayModeProperties2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetDisplayModePropertiesKHR',
    }
    _python_name_ = {
        'displayMode': 'display_mode',
        'parameters': 'parameters',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_display',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDisplayModeParametersKHR import VkDisplayModeParametersKHR

VkDisplayModePropertiesKHR._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]

VkDisplayModePropertiesKHR._type_ = {
    'displayMode': ctypes.c_void_p,
    'parameters': VkDisplayModeParametersKHR,
}
