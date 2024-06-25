import ctypes

class VkOffset2D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]

VkOffset2D._type_ = {
    'x': ctypes.c_int32,
    'y': ctypes.c_int32,
}
