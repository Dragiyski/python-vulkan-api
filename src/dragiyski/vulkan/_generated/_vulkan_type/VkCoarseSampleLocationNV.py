import ctypes

class VkCoarseSampleLocationNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'pixelX': ctypes.c_uint32,
            'pixelY': ctypes.c_uint32,
            'sample': ctypes.c_uint32,
        }

    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]
