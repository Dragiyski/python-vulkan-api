import ctypes

class VkSemaphoreSubmitInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'semaphore': ctypes.c_void_p,
            'value': ctypes.c_uint64,
            'stageMask': ctypes.c_uint64,
            'deviceIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
        ('stageMask', ctypes.c_uint64),
        ('deviceIndex', ctypes.c_uint32),
    ]
