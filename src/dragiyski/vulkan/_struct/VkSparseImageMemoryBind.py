import ctypes, sys

class VkSparseImageMemoryBind(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageMemoryBind

from . import VkExtent3D
from . import VkImageSubresource
from . import VkOffset3D

VkSparseImageMemoryBind._fields_ = [
    ('subresource', VkImageSubresource),
    ('offset', VkOffset3D),
    ('extent', VkExtent3D),
    ('memory', ctypes.c_void_p),
    ('memoryOffset', ctypes.c_uint64),
    ('flags', ctypes.c_uint32),
]
