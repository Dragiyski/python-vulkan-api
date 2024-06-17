import ctypes, sys

class VkSubresourceLayout(ctypes.Structure):
    _fields_ = [
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('rowPitch', ctypes.c_uint64),
        ('arrayPitch', ctypes.c_uint64),
        ('depthPitch', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkSubresourceLayout
