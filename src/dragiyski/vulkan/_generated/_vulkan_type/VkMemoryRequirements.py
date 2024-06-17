import ctypes, sys

class VkMemoryRequirements(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('alignment', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryRequirements
