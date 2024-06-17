import ctypes, sys

class VkCopyBufferToImageInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyBufferToImageInfo2

from . import VkBufferImageCopy2

VkCopyBufferToImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]
