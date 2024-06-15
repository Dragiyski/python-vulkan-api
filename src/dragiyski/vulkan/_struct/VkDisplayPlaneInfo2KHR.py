import ctypes, sys

class VkDisplayPlaneInfo2KHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mode', ctypes.c_void_p),
        ('planeIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDisplayPlaneInfo2KHR
