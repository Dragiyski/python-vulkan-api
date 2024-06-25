import ctypes

class StdVideoAV1GlobalMotion(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'GmType': ctypes.ARRAY(ctypes.c_uint8, 8),
            'gm_params': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8),
        }

    _fields_ = [
        ('GmType', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('gm_params', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8)),
    ]
