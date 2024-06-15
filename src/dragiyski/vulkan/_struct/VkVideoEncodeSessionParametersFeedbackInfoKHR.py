import ctypes, sys

class VkVideoEncodeSessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasOverrides', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeSessionParametersFeedbackInfoKHR
