import ctypes, sys

class VkAmigoProfilingSubmitInfoSEC(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('firstDrawTimestamp', ctypes.c_uint64),
        ('swapBufferTimestamp', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkAmigoProfilingSubmitInfoSEC
