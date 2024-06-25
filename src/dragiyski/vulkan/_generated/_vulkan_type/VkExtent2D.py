import ctypes

class VkExtent2D(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'width': ctypes.c_uint32,
            'height': ctypes.c_uint32,
        }

    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
    ]
