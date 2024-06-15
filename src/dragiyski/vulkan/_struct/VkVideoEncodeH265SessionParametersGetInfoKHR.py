import ctypes, sys

class VkVideoEncodeH265SessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('writeStdVPS', ctypes.c_uint32),
        ('writeStdSPS', ctypes.c_uint32),
        ('writeStdPPS', ctypes.c_uint32),
        ('stdVPSId', ctypes.c_uint32),
        ('stdSPSId', ctypes.c_uint32),
        ('stdPPSId', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeH265SessionParametersGetInfoKHR
