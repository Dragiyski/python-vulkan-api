import ctypes

class VkMemoryBarrier2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'srcStageMask': ctypes.c_uint64,
            'srcAccessMask': ctypes.c_uint64,
            'dstStageMask': ctypes.c_uint64,
            'dstAccessMask': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcStageMask', ctypes.c_uint64),
        ('srcAccessMask', ctypes.c_uint64),
        ('dstStageMask', ctypes.c_uint64),
        ('dstAccessMask', ctypes.c_uint64),
    ]
