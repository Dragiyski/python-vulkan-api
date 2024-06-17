import ctypes, sys

class VkFormatProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkFormatProperties2

from . import VkFormatProperties

VkFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatProperties', VkFormatProperties),
]
