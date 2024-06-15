import ctypes, sys

class VkColorBlendAdvancedEXT(ctypes.Structure):
    _fields_ = [
        ('advancedBlendOp', ctypes.c_int),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
        ('clampResults', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkColorBlendAdvancedEXT
