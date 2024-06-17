import ctypes, sys

class VkXYColorEXT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

sys.modules[__name__] = VkXYColorEXT
