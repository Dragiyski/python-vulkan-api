import ctypes

class VkSubresourceLayout(ctypes.Structure):
    _fields_ = [
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('rowPitch', ctypes.c_uint64),
        ('arrayPitch', ctypes.c_uint64),
        ('depthPitch', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkImageDrmFormatModifierExplicitCreateInfoEXT',
        'VkSubresourceLayout2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetImageSubresourceLayout',
    }
    _python_name_ = {
        'offset': 'offset',
        'size': 'size',
        'rowPitch': 'row_pitch',
        'arrayPitch': 'array_pitch',
        'depthPitch': 'depth_pitch',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkSubresourceLayout._type_ = {
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'rowPitch': ctypes.c_uint64,
    'arrayPitch': ctypes.c_uint64,
    'depthPitch': ctypes.c_uint64,
}
