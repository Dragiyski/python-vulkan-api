import ctypes

class StdVideoH265LongTermRefPicsSps(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'used_by_curr_pic_lt_sps_flag': ctypes.c_uint32,
            'lt_ref_pic_poc_lsb_sps': ctypes.ARRAY(ctypes.c_uint32, 32),
        }

    _fields_ = [
        ('used_by_curr_pic_lt_sps_flag', ctypes.c_uint32),
        ('lt_ref_pic_poc_lsb_sps', ctypes.ARRAY(ctypes.c_uint32, 32)),
    ]
