import ctypes, sys

class VkMemoryType(ctypes.Structure):
    _fields_ = [
        ('propertyFlags', ctypes.c_uint32),
        ('heapIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryType
