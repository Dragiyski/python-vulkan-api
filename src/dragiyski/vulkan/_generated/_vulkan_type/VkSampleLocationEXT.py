import ctypes, sys

class VkSampleLocationEXT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

sys.modules[__name__] = VkSampleLocationEXT
