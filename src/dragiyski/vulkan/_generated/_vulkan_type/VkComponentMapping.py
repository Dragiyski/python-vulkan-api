import ctypes

class VkComponentMapping(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'r': ctypes.c_int,
            'g': ctypes.c_int,
            'b': ctypes.c_int,
            'a': ctypes.c_int,
        }

    _fields_ = [
        ('r', ctypes.c_int),
        ('g', ctypes.c_int),
        ('b', ctypes.c_int),
        ('a', ctypes.c_int),
    ]
