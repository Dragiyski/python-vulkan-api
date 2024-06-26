import ctypes

class VkDisplayPlanePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDisplayPlaneProperties2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceDisplayPlanePropertiesKHR',
    }
    _python_name_ = {
        'currentDisplay': 'current_display',
        'currentStackIndex': 'current_stack_index',
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

VkDisplayPlanePropertiesKHR._type_ = {
    'currentDisplay': ctypes.c_void_p,
    'currentStackIndex': ctypes.c_uint32,
}
