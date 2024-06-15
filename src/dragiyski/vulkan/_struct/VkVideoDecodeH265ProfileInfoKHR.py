import ctypes, sys

class VkVideoDecodeH265ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
    ]

sys.modules[__name__] = VkVideoDecodeH265ProfileInfoKHR
