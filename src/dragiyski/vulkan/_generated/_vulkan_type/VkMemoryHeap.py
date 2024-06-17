import ctypes, sys

class VkMemoryHeap(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryHeap
