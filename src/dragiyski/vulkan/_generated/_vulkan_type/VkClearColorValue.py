import ctypes

class VkClearColorValue(ctypes.Union):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'float32': ctypes.ARRAY(ctypes.c_float, 4),
            'int32': ctypes.ARRAY(ctypes.c_int32, 4),
            'uint32': ctypes.ARRAY(ctypes.c_uint32, 4),
        }

    _fields_ = [
        ('float32', ctypes.ARRAY(ctypes.c_float, 4)),
        ('int32', ctypes.ARRAY(ctypes.c_int32, 4)),
        ('uint32', ctypes.ARRAY(ctypes.c_uint32, 4)),
    ]
