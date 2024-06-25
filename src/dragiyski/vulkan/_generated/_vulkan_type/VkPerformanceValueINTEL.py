import ctypes

class VkPerformanceValueINTEL(ctypes.Structure):
    pass

from .VkPerformanceValueDataINTEL import VkPerformanceValueDataINTEL

VkPerformanceValueINTEL._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]

VkPerformanceValueINTEL._type_ = {
    'type': ctypes.c_int,
    'data': VkPerformanceValueDataINTEL,
}
