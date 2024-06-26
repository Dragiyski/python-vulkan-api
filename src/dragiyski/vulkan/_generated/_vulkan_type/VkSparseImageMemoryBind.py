import ctypes

class VkSparseImageMemoryBind(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent3D',
        'VkImageSubresource',
        'VkOffset3D',
    }
    _included_in_ = {
        'VkSparseImageMemoryBindInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'subresource': 'subresource',
        'offset': 'offset',
        'extent': 'extent',
        'memory': 'memory',
        'memoryOffset': 'memory_offset',
        'flags': 'flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'flags': 'VkSparseMemoryBindFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent3D import VkExtent3D
from .VkImageSubresource import VkImageSubresource
from .VkOffset3D import VkOffset3D

VkSparseImageMemoryBind._fields_ = [
    ('subresource', VkImageSubresource),
    ('offset', VkOffset3D),
    ('extent', VkExtent3D),
    ('memory', ctypes.c_void_p),
    ('memoryOffset', ctypes.c_uint64),
    ('flags', ctypes.c_uint32),
]

VkSparseImageMemoryBind._type_ = {
    'subresource': VkImageSubresource,
    'offset': VkOffset3D,
    'extent': VkExtent3D,
    'memory': ctypes.c_void_p,
    'memoryOffset': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
