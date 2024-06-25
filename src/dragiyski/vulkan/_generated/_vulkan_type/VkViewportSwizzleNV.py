import ctypes

class VkViewportSwizzleNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'x': ctypes.c_int,
            'y': ctypes.c_int,
            'z': ctypes.c_int,
            'w': ctypes.c_int,
        }

    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
        ('w', ctypes.c_int),
    ]
