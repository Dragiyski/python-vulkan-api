import ctypes, sys

class VkCoarseSampleLocationNV(ctypes.Structure):
    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkCoarseSampleLocationNV
