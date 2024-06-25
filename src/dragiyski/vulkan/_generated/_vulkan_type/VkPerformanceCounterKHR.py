import ctypes

class VkPerformanceCounterKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'unit': ctypes.c_int,
            'scope': ctypes.c_int,
            'storage': ctypes.c_int,
            'uuid': ctypes.ARRAY(ctypes.c_uint8, 16),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('unit', ctypes.c_int),
        ('scope', ctypes.c_int),
        ('storage', ctypes.c_int),
        ('uuid', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]
