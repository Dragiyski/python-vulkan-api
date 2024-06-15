import ctypes, sys

class VkPushConstantRange(ctypes.Structure):
    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPushConstantRange
