import ctypes

class VkDisplayPlaneInfo2KHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'mode': ctypes.c_void_p,
            'planeIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mode', ctypes.c_void_p),
        ('planeIndex', ctypes.c_uint32),
    ]
