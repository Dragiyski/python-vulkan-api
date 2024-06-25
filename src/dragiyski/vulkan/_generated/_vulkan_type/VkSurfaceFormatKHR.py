import ctypes

class VkSurfaceFormatKHR(ctypes.Structure):
    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]

VkSurfaceFormatKHR._type_ = {
    'format': ctypes.c_int,
    'colorSpace': ctypes.c_int,
}
