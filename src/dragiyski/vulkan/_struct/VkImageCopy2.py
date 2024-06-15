import ctypes, sys

class VkImageCopy2(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageCopy2

from . import VkExtent3D
from . import VkImageSubresourceLayers
from . import VkOffset3D

VkImageCopy2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcSubresource', VkImageSubresourceLayers),
    ('srcOffset', VkOffset3D),
    ('dstSubresource', VkImageSubresourceLayers),
    ('dstOffset', VkOffset3D),
    ('extent', VkExtent3D),
]
