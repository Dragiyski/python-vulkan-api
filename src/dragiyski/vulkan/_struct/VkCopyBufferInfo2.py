import ctypes, sys

class VkCopyBufferInfo2(ctypes.Structure):
    pass

sys.modules[__name__] = VkCopyBufferInfo2

from . import VkBufferCopy2

VkCopyBufferInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferCopy2)),
]
