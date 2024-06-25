import ctypes

class VkBindMemoryStatusKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pResult': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pResult', ctypes.POINTER(ctypes.c_int)),
    ]
