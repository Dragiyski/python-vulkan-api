import ctypes

class VkOffset2D(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'x': ctypes.c_int32,
            'y': ctypes.c_int32,
        }

    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
    ]
