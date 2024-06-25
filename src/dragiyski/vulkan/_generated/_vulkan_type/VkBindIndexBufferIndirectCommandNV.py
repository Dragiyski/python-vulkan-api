import ctypes

class VkBindIndexBufferIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
    ]

VkBindIndexBufferIndirectCommandNV._type_ = {
    'bufferAddress': ctypes.c_uint64,
    'size': ctypes.c_uint32,
    'indexType': ctypes.c_int,
}
