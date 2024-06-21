import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearColorValue import CType as VkClearColorValue

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('customBorderColor', VkClearColorValue),
    ('format', ctypes.c_int),
]
