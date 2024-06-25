import ctypes

class VkMemoryHeap(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'size': ctypes.c_uint64,
            'flags': ctypes.c_uint32,
        }

    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]
