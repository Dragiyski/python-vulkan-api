import ctypes, sys

class VkMemoryToImageCopyEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkMemoryToImageCopyEXT

from . import VkImageSubresourceLayers
from . import VkOffset3D
from . import VkExtent3D

VkMemoryToImageCopyEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pHostPointer', ctypes.c_void_p),
    ('memoryRowLength', ctypes.c_uint32),
    ('memoryImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
