import ctypes

class VkSubpassDependency(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'srcSubpass': ctypes.c_uint32,
            'dstSubpass': ctypes.c_uint32,
            'srcStageMask': ctypes.c_uint32,
            'dstStageMask': ctypes.c_uint32,
            'srcAccessMask': ctypes.c_uint32,
            'dstAccessMask': ctypes.c_uint32,
            'dependencyFlags': ctypes.c_uint32,
        }

    _fields_ = [
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
    ]
