import ctypes, sys

class VkIOSSurfaceCreateInfoMVK(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('pView', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkIOSSurfaceCreateInfoMVK
