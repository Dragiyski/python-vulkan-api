import ctypes

class VkSurfaceFormatKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'format': ctypes.c_int,
            'colorSpace': ctypes.c_int,
        }

    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]
