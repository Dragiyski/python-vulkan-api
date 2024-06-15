import ctypes, sys

class VkSparseMemoryBind(ctypes.Structure):
    _fields_ = [
        ('resourceOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSparseMemoryBind
