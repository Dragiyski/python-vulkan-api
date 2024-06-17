import ctypes, sys

class VkOffset2D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]

sys.modules[__name__] = VkOffset2D
