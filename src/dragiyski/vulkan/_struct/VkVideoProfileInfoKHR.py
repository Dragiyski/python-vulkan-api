import ctypes, sys

class VkVideoProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoCodecOperation', ctypes.c_uint32),
        ('chromaSubsampling', ctypes.c_uint32),
        ('lumaBitDepth', ctypes.c_uint32),
        ('chromaBitDepth', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoProfileInfoKHR
