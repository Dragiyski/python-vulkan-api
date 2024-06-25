import ctypes

class VkViewportSwizzleNV(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
        ('w', ctypes.c_int),
    ]

VkViewportSwizzleNV._type_ = {
    'x': ctypes.c_int,
    'y': ctypes.c_int,
    'z': ctypes.c_int,
    'w': ctypes.c_int,
}
