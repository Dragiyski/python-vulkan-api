import ctypes, sys

class VkDirectFBSurfaceCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dfb', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkDirectFBSurfaceCreateInfoEXT
