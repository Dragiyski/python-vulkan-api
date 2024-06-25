import ctypes

class VkPerformanceCounterKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('unit', ctypes.c_int),
        ('scope', ctypes.c_int),
        ('storage', ctypes.c_int),
        ('uuid', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

VkPerformanceCounterKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'unit': ctypes.c_int,
    'scope': ctypes.c_int,
    'storage': ctypes.c_int,
    'uuid': ctypes.ARRAY(ctypes.c_uint8, 16),
}
