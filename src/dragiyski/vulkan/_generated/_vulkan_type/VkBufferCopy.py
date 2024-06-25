import ctypes

class VkBufferCopy(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'srcOffset': ctypes.c_uint64,
            'dstOffset': ctypes.c_uint64,
            'size': ctypes.c_uint64,
        }

    _fields_ = [
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
