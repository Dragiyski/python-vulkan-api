import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('inter_ref_pic_set_prediction_flag', ctypes.c_uint32, 1),
        ('delta_rps_sign', ctypes.c_uint32, 1),
    ]
