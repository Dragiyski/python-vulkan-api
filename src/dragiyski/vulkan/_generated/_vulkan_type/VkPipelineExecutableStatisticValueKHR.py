import ctypes

class VkPipelineExecutableStatisticValueKHR(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'b32': ctypes.c_uint32,
            'i64': ctypes.c_int64,
            'u64': ctypes.c_uint64,
            'f64': ctypes.c_double,
        }

    _fields_ = [
        ('b32', ctypes.c_uint32),
        ('i64', ctypes.c_int64),
        ('u64', ctypes.c_uint64),
        ('f64', ctypes.c_double),
    ]
