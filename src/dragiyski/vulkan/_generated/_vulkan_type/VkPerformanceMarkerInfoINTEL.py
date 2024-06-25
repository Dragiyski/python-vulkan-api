import ctypes

class VkPerformanceMarkerInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('marker', ctypes.c_uint64),
    ]

VkPerformanceMarkerInfoINTEL._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'marker': ctypes.c_uint64,
}
