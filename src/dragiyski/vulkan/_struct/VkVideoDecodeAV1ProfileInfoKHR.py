import ctypes, sys

class VkVideoDecodeAV1ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfile', ctypes.c_int),
        ('filmGrainSupport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoDecodeAV1ProfileInfoKHR
