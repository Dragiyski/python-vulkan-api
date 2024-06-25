import ctypes

class VkMemoryBarrier2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcStageMask', ctypes.c_uint64),
        ('srcAccessMask', ctypes.c_uint64),
        ('dstStageMask', ctypes.c_uint64),
        ('dstAccessMask', ctypes.c_uint64),
    ]

VkMemoryBarrier2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcStageMask': ctypes.c_uint64,
    'srcAccessMask': ctypes.c_uint64,
    'dstStageMask': ctypes.c_uint64,
    'dstAccessMask': ctypes.c_uint64,
}
