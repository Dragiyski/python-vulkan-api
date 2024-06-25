import ctypes

class VkXYColorEXT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

VkXYColorEXT._type_ = {
    'x': ctypes.c_float,
    'y': ctypes.c_float,
}
