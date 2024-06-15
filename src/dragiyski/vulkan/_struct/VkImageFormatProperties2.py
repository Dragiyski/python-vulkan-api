import ctypes, sys

class VkImageFormatProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageFormatProperties2

from . import VkImageFormatProperties

VkImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]
