import ctypes

class VkIndirectCommandsStreamNV(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
    ]

VkIndirectCommandsStreamNV._type_ = {
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
}
