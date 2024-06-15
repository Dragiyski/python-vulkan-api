import ctypes, sys

class VkCopyMicromapInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('src', ctypes.c_void_p),
        ('dst', ctypes.c_void_p),
        ('mode', ctypes.c_int),
    ]

sys.modules[__name__] = VkCopyMicromapInfoEXT
