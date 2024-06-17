import ctypes, sys

class VkVideoEncodeSessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoSessionParameters', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkVideoEncodeSessionParametersGetInfoKHR
