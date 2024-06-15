import ctypes, sys

class VkApplicationInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pApplicationName', ctypes.c_char_p),
        ('applicationVersion', ctypes.c_uint32),
        ('pEngineName', ctypes.c_char_p),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkApplicationInfo
