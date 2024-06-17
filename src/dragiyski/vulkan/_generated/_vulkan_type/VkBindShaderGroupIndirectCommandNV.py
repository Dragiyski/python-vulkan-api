import ctypes, sys

class VkBindShaderGroupIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkBindShaderGroupIndirectCommandNV
