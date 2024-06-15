import ctypes, sys

class VkExtent2D(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkExtent2D
