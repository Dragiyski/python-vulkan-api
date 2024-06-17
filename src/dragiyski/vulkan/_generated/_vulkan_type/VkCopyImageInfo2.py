import ctypes, sys

class VkCopyImageInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyImageInfo2

from . import VkImageCopy2

VkCopyImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageCopy2)),
]
