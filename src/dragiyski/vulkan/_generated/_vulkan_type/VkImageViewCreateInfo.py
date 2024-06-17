import ctypes, sys

class VkImageViewCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageViewCreateInfo

from . import VkComponentMapping
from . import VkImageSubresourceRange

VkImageViewCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('viewType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('components', VkComponentMapping),
    ('subresourceRange', VkImageSubresourceRange),
]
