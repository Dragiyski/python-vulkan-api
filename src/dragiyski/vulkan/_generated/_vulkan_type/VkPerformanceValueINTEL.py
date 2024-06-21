import ctypes

class CType(ctypes.Structure):
    pass

from .VkPerformanceValueDataINTEL import CType as VkPerformanceValueDataINTEL

CType._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]
