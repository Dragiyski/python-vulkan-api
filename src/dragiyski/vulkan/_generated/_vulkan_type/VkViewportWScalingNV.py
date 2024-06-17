import ctypes, sys

class VkViewportWScalingNV(ctypes.Structure):
    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]

sys.modules[__name__] = VkViewportWScalingNV
