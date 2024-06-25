import ctypes

class StdVideoDecodeH265PictureInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'IrapPicFlag': ctypes.c_uint32,
            'IdrPicFlag': ctypes.c_uint32,
            'IsReference': ctypes.c_uint32,
            'short_term_ref_pic_set_sps_flag': ctypes.c_uint32,
        }

    _fields_ = [
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('IsReference', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
    ]
