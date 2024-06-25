import ctypes

class VkCopyMemoryIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'srcAddress': ctypes.c_uint64,
            'dstAddress': ctypes.c_uint64,
            'size': ctypes.c_uint64,
        }

    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
