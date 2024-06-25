import ctypes

class VkSparseMemoryBind(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'resourceOffset': ctypes.c_uint64,
            'size': ctypes.c_uint64,
            'memory': ctypes.c_void_p,
            'memoryOffset': ctypes.c_uint64,
            'flags': ctypes.c_uint32,
        }

    _fields_ = [
        ('resourceOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]
