import ctypes

class VkViewportSwizzleNV(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
        ('w', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineViewportSwizzleStateCreateInfoNV',
    }
    _input_of_ = {
        'vkCmdSetViewportSwizzleNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'w': 'w',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_viewport_swizzle',
    }
    _vk_enum_ = {
        'x': 'VkViewportCoordinateSwizzleNV',
        'y': 'VkViewportCoordinateSwizzleNV',
        'z': 'VkViewportCoordinateSwizzleNV',
        'w': 'VkViewportCoordinateSwizzleNV',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkViewportSwizzleNV._type_ = {
    'x': ctypes.c_int,
    'y': ctypes.c_int,
    'z': ctypes.c_int,
    'w': ctypes.c_int,
}
