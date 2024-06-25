import ctypes

class VkDisplayPlanePropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'currentDisplay': ctypes.c_void_p,
            'currentStackIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]
