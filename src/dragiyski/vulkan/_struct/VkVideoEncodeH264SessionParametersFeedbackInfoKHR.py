import ctypes, sys

class VkVideoEncodeH264SessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeH264SessionParametersFeedbackInfoKHR
