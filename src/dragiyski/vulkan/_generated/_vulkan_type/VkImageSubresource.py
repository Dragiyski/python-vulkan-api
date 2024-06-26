import ctypes

class VkImageSubresource(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('arrayLayer', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkImageSubresource2KHR',
        'VkSparseImageMemoryBind',
    }
    _input_of_ = {
        'vkGetImageSubresourceLayout',
    }
    _output_of_ = set()
    _python_name_ = {
        'aspectMask': 'aspect_mask',
        'mipLevel': 'mip_level',
        'arrayLayer': 'array_layer',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'aspectMask': 'VkImageAspectFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkImageSubresource._type_ = {
    'aspectMask': ctypes.c_uint32,
    'mipLevel': ctypes.c_uint32,
    'arrayLayer': ctypes.c_uint32,
}
