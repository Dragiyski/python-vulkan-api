import ctypes

class VkMemoryHeap(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

VkMemoryHeap._type_ = {
    'size': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
