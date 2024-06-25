import ctypes

class VkSubresourceLayout(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'offset': ctypes.c_uint64,
            'size': ctypes.c_uint64,
            'rowPitch': ctypes.c_uint64,
            'arrayPitch': ctypes.c_uint64,
            'depthPitch': ctypes.c_uint64,
        }

    _fields_ = [
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('rowPitch', ctypes.c_uint64),
        ('arrayPitch', ctypes.c_uint64),
        ('depthPitch', ctypes.c_uint64),
    ]
