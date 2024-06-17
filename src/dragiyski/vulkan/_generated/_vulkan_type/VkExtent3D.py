import ctypes, sys

class VkExtent3D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExtent3D
