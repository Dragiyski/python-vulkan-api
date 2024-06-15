import ctypes, sys

class VkSparseImageFormatProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkSparseImageFormatProperties

from . import VkExtent3D

VkSparseImageFormatProperties._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]
