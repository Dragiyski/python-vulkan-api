import ctypes, sys

class VkSparseImageFormatProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageFormatProperties2

from . import VkSparseImageFormatProperties

VkSparseImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkSparseImageFormatProperties),
]
