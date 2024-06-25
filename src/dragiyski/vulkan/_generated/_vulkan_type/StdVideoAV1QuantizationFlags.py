import ctypes

class StdVideoAV1QuantizationFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'using_qmatrix': ctypes.c_uint32,
            'diff_uv_delta': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]
