import ctypes

class VkSemaphoreWaitInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'semaphoreCount': ctypes.c_uint32,
            'pSemaphores': ctypes.POINTER(ctypes.c_void_p),
            'pValues': ctypes.POINTER(ctypes.c_uint64),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('semaphoreCount', ctypes.c_uint32),
        ('pSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pValues', ctypes.POINTER(ctypes.c_uint64)),
    ]
