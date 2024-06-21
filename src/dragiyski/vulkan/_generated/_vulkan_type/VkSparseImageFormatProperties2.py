import ctypes

class CType(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import CType as VkSparseImageFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkSparseImageFormatProperties),
]
