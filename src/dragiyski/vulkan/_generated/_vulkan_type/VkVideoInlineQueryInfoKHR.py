import ctypes, sys

class VkVideoInlineQueryInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryPool', ctypes.c_void_p),
        ('firstQuery', ctypes.c_uint32),
        ('queryCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoInlineQueryInfoKHR
