import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('used_by_curr_pic_lt_sps_flag', ctypes.c_uint32),
        ('lt_ref_pic_poc_lsb_sps', ctypes.ARRAY(ctypes.c_uint32, 32)),
    ]
