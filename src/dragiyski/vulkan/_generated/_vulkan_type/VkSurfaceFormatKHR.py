import ctypes

class VkSurfaceFormatKHR(ctypes.Structure):
    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkSurfaceFormat2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSurfaceFormatsKHR',
    }
    _python_name_ = {
        'format': 'format',
        'colorSpace': 'color_space',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_surface',
    }
    _vk_enum_ = {
        'format': 'VkFormat',
        'colorSpace': 'VkColorSpaceKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkSurfaceFormatKHR._type_ = {
    'format': ctypes.c_int,
    'colorSpace': ctypes.c_int,
}
