import ctypes, sys

class VkAabbPositionsKHR(ctypes.Structure):
    _fields_ = [
        ('minX', ctypes.c_float),
        ('minY', ctypes.c_float),
        ('minZ', ctypes.c_float),
        ('maxX', ctypes.c_float),
        ('maxY', ctypes.c_float),
        ('maxZ', ctypes.c_float),
    ]

sys.modules[__name__] = VkAabbPositionsKHR
