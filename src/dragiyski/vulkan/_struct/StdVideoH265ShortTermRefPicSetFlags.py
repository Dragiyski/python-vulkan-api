import ctypes, sys

class StdVideoH265ShortTermRefPicSetFlags(ctypes.Structure):
    _fields_ = [
        ('inter_ref_pic_set_prediction_flag', ctypes.c_uint32, 1),
        ('delta_rps_sign', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoH265ShortTermRefPicSetFlags
