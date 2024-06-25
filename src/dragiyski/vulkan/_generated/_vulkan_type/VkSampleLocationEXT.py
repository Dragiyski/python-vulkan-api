import ctypes

class VkSampleLocationEXT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

VkSampleLocationEXT._type_ = {
    'x': ctypes.c_float,
    'y': ctypes.c_float,
}
