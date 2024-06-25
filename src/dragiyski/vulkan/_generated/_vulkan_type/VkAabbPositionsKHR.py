import ctypes

class VkAabbPositionsKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'minX': ctypes.c_float,
            'minY': ctypes.c_float,
            'minZ': ctypes.c_float,
            'maxX': ctypes.c_float,
            'maxY': ctypes.c_float,
            'maxZ': ctypes.c_float,
        }

    _fields_ = [
        ('minX', ctypes.c_float),
        ('minY', ctypes.c_float),
        ('minZ', ctypes.c_float),
        ('maxX', ctypes.c_float),
        ('maxY', ctypes.c_float),
        ('maxZ', ctypes.c_float),
    ]
