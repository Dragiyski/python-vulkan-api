import ctypes

class VkSubpassDependency2(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'srcSubpass': ctypes.c_uint32,
            'dstSubpass': ctypes.c_uint32,
            'srcStageMask': ctypes.c_uint32,
            'dstStageMask': ctypes.c_uint32,
            'srcAccessMask': ctypes.c_uint32,
            'dstAccessMask': ctypes.c_uint32,
            'dependencyFlags': ctypes.c_uint32,
            'viewOffset': ctypes.c_int32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
        ('viewOffset', ctypes.c_int32),
    ]
