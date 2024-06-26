import ctypes

class VkDisplayModeParametersKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = {
        'VkDisplayModeCreateInfoKHR',
        'VkDisplayModePropertiesKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'visibleRegion': 'visible_region',
        'refreshRate': 'refresh_rate',
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


from .VkExtent2D import VkExtent2D

VkDisplayModeParametersKHR._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]

VkDisplayModeParametersKHR._type_ = {
    'visibleRegion': VkExtent2D,
    'refreshRate': ctypes.c_uint32,
}
