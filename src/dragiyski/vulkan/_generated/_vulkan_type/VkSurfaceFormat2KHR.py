import ctypes

class CType(ctypes.Structure):
    pass

from .VkSurfaceFormatKHR import CType as VkSurfaceFormatKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]
