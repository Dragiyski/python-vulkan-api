import ctypes, sys

class VkVideoSessionParametersCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('videoSessionParametersTemplate', ctypes.c_void_p),
        ('videoSession', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkVideoSessionParametersCreateInfoKHR
