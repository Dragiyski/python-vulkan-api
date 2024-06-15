import ctypes, sys

class VkImageSubresource2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageSubresource2KHR

from . import VkImageSubresource

VkImageSubresource2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageSubresource', VkImageSubresource),
]
