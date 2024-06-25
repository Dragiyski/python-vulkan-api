import ctypes

class VkPerformanceStreamMarkerInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('marker', ctypes.c_uint32),
    ]

VkPerformanceStreamMarkerInfoINTEL._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'marker': ctypes.c_uint32,
}
