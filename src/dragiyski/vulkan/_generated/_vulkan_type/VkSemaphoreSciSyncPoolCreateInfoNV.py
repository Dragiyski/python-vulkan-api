import ctypes, sys

class VkSemaphoreSciSyncPoolCreateInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handle', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkSemaphoreSciSyncPoolCreateInfoNV
