import ctypes

class VkTimelineSemaphoreSubmitInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'waitSemaphoreValueCount': ctypes.c_uint32,
            'pWaitSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
            'signalSemaphoreValueCount': ctypes.c_uint32,
            'pSignalSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValueCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValueCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]
