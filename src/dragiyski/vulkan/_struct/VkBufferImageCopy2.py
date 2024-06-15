import ctypes, sys

class VkBufferImageCopy2(ctypes.Structure):
    pass

sys.modules[__name__] = VkBufferImageCopy2

from . import VkImageSubresourceLayers
from . import VkOffset3D
from . import VkExtent3D

VkBufferImageCopy2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]
