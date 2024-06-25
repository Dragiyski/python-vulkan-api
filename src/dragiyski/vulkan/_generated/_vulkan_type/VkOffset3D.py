import ctypes

class VkOffset3D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('z', ctypes.c_int32),
    ]

VkOffset3D._type_ = {
    'x': ctypes.c_int32,
    'y': ctypes.c_int32,
    'z': ctypes.c_int32,
}
