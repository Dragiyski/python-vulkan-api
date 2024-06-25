import ctypes

class VkSparseImageMemoryBind(ctypes.Structure):
    pass

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
