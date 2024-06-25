import ctypes

class VkSemaphoreSciSyncCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'semaphorePool': ctypes.c_void_p,
            'pFence': ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6)),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphorePool', ctypes.c_void_p),
        ('pFence', ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6))),
    ]
