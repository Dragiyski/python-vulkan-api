import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryToImageCopyEXT import CType as VkMemoryToImageCopyEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkMemoryToImageCopyEXT)),
]
