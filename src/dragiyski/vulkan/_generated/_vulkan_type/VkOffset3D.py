import ctypes, sys

class VkOffset3D(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ('z', ctypes.c_int32),
    ]

sys.modules[__name__] = VkOffset3D
