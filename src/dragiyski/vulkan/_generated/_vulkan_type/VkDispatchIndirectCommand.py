import ctypes

class VkDispatchIndirectCommand(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'x': ctypes.c_uint32,
            'y': ctypes.c_uint32,
            'z': ctypes.c_uint32,
        }

    _fields_ = [
        ('x', ctypes.c_uint32),
        ('y', ctypes.c_uint32),
        ('z', ctypes.c_uint32),
    ]
