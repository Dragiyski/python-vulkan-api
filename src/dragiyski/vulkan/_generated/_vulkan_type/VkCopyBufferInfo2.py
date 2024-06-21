import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCopy2 import CType as VkBufferCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferCopy2)),
]
