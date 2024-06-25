import ctypes

class VkNativeBufferUsage2ANDROID(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'consumer': ctypes.c_uint64,
            'producer': ctypes.c_uint64,
        }

    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]
