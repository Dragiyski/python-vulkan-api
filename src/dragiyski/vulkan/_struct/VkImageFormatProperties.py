import ctypes, sys

class VkImageFormatProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageFormatProperties

from . import VkExtent3D

VkImageFormatProperties._fields_ = [
    ('maxExtent', VkExtent3D),
    ('maxMipLevels', ctypes.c_uint32),
    ('maxArrayLayers', ctypes.c_uint32),
    ('sampleCounts', ctypes.c_uint32),
    ('maxResourceSize', ctypes.c_uint64),
]
