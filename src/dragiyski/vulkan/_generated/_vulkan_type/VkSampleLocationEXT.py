import ctypes

class VkSampleLocationEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'x': ctypes.c_float,
            'y': ctypes.c_float,
        }

    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]
