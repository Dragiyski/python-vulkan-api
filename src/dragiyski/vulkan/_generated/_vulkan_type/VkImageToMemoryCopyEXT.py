import ctypes, sys

class VkImageToMemoryCopyEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageToMemoryCopyEXT

from . import VkExtent3D
from . import VkImageSubresourceLayers
from . import VkOffset3D

VkImageToMemoryCopyEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pHostPointer', ctypes.c_void_p),
    ('memoryRowLength', ctypes.c_uint32),
    ('memoryImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
