import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageFormatProperties import CType as VkImageFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]
