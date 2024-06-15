import ctypes, sys

class VkVideoDecodeH264ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
        ('pictureLayout', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoDecodeH264ProfileInfoKHR
