import ctypes, sys

class VkVideoEncodeH265SessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdVPSOverrides', ctypes.c_uint32),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeH265SessionParametersFeedbackInfoKHR
