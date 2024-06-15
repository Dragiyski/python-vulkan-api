import ctypes, sys

class VkFormatProperties(ctypes.Structure):
    _fields_ = [
        ('linearTilingFeatures', ctypes.c_uint32),
        ('optimalTilingFeatures', ctypes.c_uint32),
        ('bufferFeatures', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkFormatProperties
