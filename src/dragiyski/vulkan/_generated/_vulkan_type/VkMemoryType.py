import ctypes

class VkMemoryType(ctypes.Structure):
    _fields_ = [
        ('propertyFlags', ctypes.c_uint32),
        ('heapIndex', ctypes.c_uint32),
    ]

VkMemoryType._type_ = {
    'propertyFlags': ctypes.c_uint32,
    'heapIndex': ctypes.c_uint32,
}
