import ctypes

class VkTransformMatrixKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'matrix': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3),
        }

    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]
