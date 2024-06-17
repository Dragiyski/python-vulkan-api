import ctypes, sys

class VkDrmFormatModifierProperties2EXT(ctypes.Structure):
    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkDrmFormatModifierProperties2EXT
