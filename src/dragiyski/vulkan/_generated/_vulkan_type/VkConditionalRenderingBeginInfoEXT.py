import ctypes

class VkConditionalRenderingBeginInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

VkConditionalRenderingBeginInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
