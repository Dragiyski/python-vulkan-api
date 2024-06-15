import ctypes, sys

class VkPerformanceValueINTEL(ctypes.Structure):
    pass

sys.modules[__name__] = VkPerformanceValueINTEL

from . import VkPerformanceValueDataINTEL

VkPerformanceValueINTEL._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]
