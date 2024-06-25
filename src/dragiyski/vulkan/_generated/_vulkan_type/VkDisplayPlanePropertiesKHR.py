import ctypes

class VkDisplayPlanePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]

VkDisplayPlanePropertiesKHR._type_ = {
    'currentDisplay': ctypes.c_void_p,
    'currentStackIndex': ctypes.c_uint32,
}
