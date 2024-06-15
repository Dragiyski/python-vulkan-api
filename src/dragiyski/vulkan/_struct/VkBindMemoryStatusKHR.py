import ctypes, sys

class VkBindMemoryStatusKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pResult', ctypes.POINTER(ctypes.c_int)),
    ]

sys.modules[__name__] = VkBindMemoryStatusKHR
