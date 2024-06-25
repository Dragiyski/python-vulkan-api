import ctypes

class VkVideoEncodeH264QpKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'qpI': ctypes.c_int32,
            'qpP': ctypes.c_int32,
            'qpB': ctypes.c_int32,
        }

    _fields_ = [
        ('qpI', ctypes.c_int32),
        ('qpP', ctypes.c_int32),
        ('qpB', ctypes.c_int32),
    ]
