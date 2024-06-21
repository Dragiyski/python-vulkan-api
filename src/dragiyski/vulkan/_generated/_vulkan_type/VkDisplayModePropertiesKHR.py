import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import CType as VkDisplayModeParametersKHR

CType._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]
