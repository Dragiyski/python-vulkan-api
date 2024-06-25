import ctypes

class VkViewportWScalingNV(ctypes.Structure):
    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]

VkViewportWScalingNV._type_ = {
    'xcoeff': ctypes.c_float,
    'ycoeff': ctypes.c_float,
}
