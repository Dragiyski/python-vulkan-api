import ctypes

class VkVideoSessionParametersCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('videoSessionParametersTemplate', ctypes.c_void_p),
        ('videoSession', ctypes.c_void_p),
    ]

VkVideoSessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'videoSessionParametersTemplate': ctypes.c_void_p,
    'videoSession': ctypes.c_void_p,
}
