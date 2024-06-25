import ctypes

class StdVideoEncodeH264PictureInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'IdrPicFlag': ctypes.c_uint32,
            'is_reference': ctypes.c_uint32,
            'no_output_of_prior_pics_flag': ctypes.c_uint32,
            'long_term_reference_flag': ctypes.c_uint32,
            'adaptive_ref_pic_marking_mode_flag': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('long_term_reference_flag', ctypes.c_uint32, 1),
        ('adaptive_ref_pic_marking_mode_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 27),
    ]
