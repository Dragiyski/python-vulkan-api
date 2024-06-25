import ctypes

class VkCopyMemoryIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

VkCopyMemoryIndirectCommandNV._type_ = {
    'srcAddress': ctypes.c_uint64,
    'dstAddress': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
