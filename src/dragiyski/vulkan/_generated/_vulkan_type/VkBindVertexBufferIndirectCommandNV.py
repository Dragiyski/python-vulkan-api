import ctypes

class VkBindVertexBufferIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
    ]

VkBindVertexBufferIndirectCommandNV._type_ = {
    'bufferAddress': ctypes.c_uint64,
    'size': ctypes.c_uint32,
    'stride': ctypes.c_uint32,
}
