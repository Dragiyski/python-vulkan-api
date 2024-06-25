import ctypes

class VkSetStateFlagsIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.c_uint32),
    ]

VkSetStateFlagsIndirectCommandNV._type_ = {
    'data': ctypes.c_uint32,
}
