import ctypes

class VkViewportWScalingNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'xcoeff': ctypes.c_float,
            'ycoeff': ctypes.c_float,
        }

    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]
