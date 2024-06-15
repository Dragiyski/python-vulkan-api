import ctypes, sys

class VkCopyImageToMemoryInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyImageToMemoryInfoEXT

from . import VkImageToMemoryCopyEXT

VkCopyImageToMemoryInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageToMemoryCopyEXT)),
]
