import ctypes

class VkQueryPoolPerformanceQueryCreateInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCountersSampling', ctypes.c_int),
    ]

VkQueryPoolPerformanceQueryCreateInfoINTEL._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'performanceCountersSampling': ctypes.c_int,
}
