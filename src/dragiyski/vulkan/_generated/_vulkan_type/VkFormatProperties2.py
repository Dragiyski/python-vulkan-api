import ctypes

class CType(ctypes.Structure):
    pass

from .VkFormatProperties import CType as VkFormatProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatProperties', VkFormatProperties),
]
