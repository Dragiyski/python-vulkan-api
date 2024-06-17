import ctypes, sys

class VkResolveImageInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkResolveImageInfo2

from . import VkImageResolve2

VkResolveImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageResolve2)),
]
