import ctypes, sys

class VkCopyMemoryIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkCopyMemoryIndirectCommandNV
