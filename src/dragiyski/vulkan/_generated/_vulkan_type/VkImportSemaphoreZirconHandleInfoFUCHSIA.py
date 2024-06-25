import ctypes

class VkImportSemaphoreZirconHandleInfoFUCHSIA(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'semaphore': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'handleType': ctypes.c_uint32,
            'zirconHandle': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('zirconHandle', ctypes.c_uint32),
    ]
