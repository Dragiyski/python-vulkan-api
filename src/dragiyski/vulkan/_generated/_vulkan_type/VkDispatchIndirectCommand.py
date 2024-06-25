import ctypes

class VkDispatchIndirectCommand(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_uint32),
        ('y', ctypes.c_uint32),
        ('z', ctypes.c_uint32),
    ]

VkDispatchIndirectCommand._type_ = {
    'x': ctypes.c_uint32,
    'y': ctypes.c_uint32,
    'z': ctypes.c_uint32,
}
