import ctypes, sys

class VkComponentMapping(ctypes.Structure):
    _fields_ = [
        ('r', ctypes.c_int),
        ('g', ctypes.c_int),
        ('b', ctypes.c_int),
        ('a', ctypes.c_int),
    ]

sys.modules[__name__] = VkComponentMapping
