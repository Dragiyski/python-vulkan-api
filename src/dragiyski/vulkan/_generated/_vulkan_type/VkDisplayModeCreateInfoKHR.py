import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import CType as VkDisplayModeParametersKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('parameters', VkDisplayModeParametersKHR),
]
