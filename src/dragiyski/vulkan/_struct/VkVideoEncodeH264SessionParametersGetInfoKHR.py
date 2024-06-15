import ctypes, sys

class VkVideoEncodeH264SessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('writeStdSPS', ctypes.c_uint32),
        ('writeStdPPS', ctypes.c_uint32),
        ('stdSPSId', ctypes.c_uint32),
        ('stdPPSId', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeH264SessionParametersGetInfoKHR
