import ctypes

class VkVideoEncodeH264SessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]

VkVideoEncodeH264SessionParametersFeedbackInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hasStdSPSOverrides': ctypes.c_uint32,
    'hasStdPPSOverrides': ctypes.c_uint32,
}
