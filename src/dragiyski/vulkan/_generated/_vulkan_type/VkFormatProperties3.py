import ctypes, sys

class VkFormatProperties3(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearTilingFeatures', ctypes.c_uint64),
        ('optimalTilingFeatures', ctypes.c_uint64),
        ('bufferFeatures', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkFormatProperties3
