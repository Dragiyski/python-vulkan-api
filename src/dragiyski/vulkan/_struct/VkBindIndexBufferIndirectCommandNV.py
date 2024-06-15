import ctypes, sys

class VkBindIndexBufferIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
    ]

sys.modules[__name__] = VkBindIndexBufferIndirectCommandNV
