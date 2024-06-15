import ctypes, sys

class VkScreenSurfaceCreateInfoQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('context', ctypes.c_void_p),
        ('window', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkScreenSurfaceCreateInfoQNX
