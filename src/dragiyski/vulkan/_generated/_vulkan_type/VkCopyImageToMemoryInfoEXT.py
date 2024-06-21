import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageToMemoryCopyEXT import CType as VkImageToMemoryCopyEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageToMemoryCopyEXT)),
]
