import ctypes

class VkAmigoProfilingSubmitInfoSEC(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'firstDrawTimestamp': ctypes.c_uint64,
            'swapBufferTimestamp': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('firstDrawTimestamp', ctypes.c_uint64),
        ('swapBufferTimestamp', ctypes.c_uint64),
    ]
