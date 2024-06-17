import ctypes, sys

class VkSetStateFlagsIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSetStateFlagsIndirectCommandNV
