import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferImageCopy2 import CType as VkBufferImageCopy2

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]
