import ctypes

class VkRefreshObjectKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'objectType': ctypes.c_int,
            'objectHandle': ctypes.c_uint64,
            'flags': ctypes.c_uint32,
        }

    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]
