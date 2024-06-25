import ctypes

class VkPerformanceCounterDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('category', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

VkPerformanceCounterDescriptionKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'category': ctypes.ARRAY(ctypes.c_char, 256),
    'description': ctypes.ARRAY(ctypes.c_char, 256),
}
