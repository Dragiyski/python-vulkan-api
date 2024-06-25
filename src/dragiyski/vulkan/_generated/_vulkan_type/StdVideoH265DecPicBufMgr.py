import ctypes

class StdVideoH265DecPicBufMgr(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'max_latency_increase_plus1': ctypes.ARRAY(ctypes.c_uint32, 7),
            'max_dec_pic_buffering_minus1': ctypes.ARRAY(ctypes.c_uint8, 7),
            'max_num_reorder_pics': ctypes.ARRAY(ctypes.c_uint8, 7),
        }

    _fields_ = [
        ('max_latency_increase_plus1', ctypes.ARRAY(ctypes.c_uint32, 7)),
        ('max_dec_pic_buffering_minus1', ctypes.ARRAY(ctypes.c_uint8, 7)),
        ('max_num_reorder_pics', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ]
