import ctypes

class VkVideoEncodeUsageInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
        ('videoContentHints', ctypes.c_uint32),
        ('tuningMode', ctypes.c_int),
    ]

VkVideoEncodeUsageInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoUsageHints': ctypes.c_uint32,
    'videoContentHints': ctypes.c_uint32,
    'tuningMode': ctypes.c_int,
}
