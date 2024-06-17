import ctypes, sys

class VkBufferImageCopy(ctypes.Structure):
    pass

sys.modules[__name__] = VkBufferImageCopy

from . import VkExtent3D
from . import VkImageSubresourceLayers
from . import VkOffset3D

VkBufferImageCopy._fields_ = [
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
