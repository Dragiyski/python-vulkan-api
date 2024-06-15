import ctypes, sys

class VkCopyMemoryToImageInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyMemoryToImageInfoEXT

from . import VkMemoryToImageCopyEXT

VkCopyMemoryToImageInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkMemoryToImageCopyEXT)),
]
