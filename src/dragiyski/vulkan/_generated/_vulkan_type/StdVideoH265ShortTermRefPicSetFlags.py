import ctypes

class StdVideoH265ShortTermRefPicSetFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'inter_ref_pic_set_prediction_flag': ctypes.c_uint32,
            'delta_rps_sign': ctypes.c_uint32,
        }

    _fields_ = [
        ('inter_ref_pic_set_prediction_flag', ctypes.c_uint32, 1),
        ('delta_rps_sign', ctypes.c_uint32, 1),
    ]
