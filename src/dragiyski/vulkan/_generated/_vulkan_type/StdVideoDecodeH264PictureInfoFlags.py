import ctypes

class StdVideoDecodeH264PictureInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'field_pic_flag': ctypes.c_uint32,
            'is_intra': ctypes.c_uint32,
            'IdrPicFlag': ctypes.c_uint32,
            'bottom_field_flag': ctypes.c_uint32,
            'is_reference': ctypes.c_uint32,
            'complementary_field_pair': ctypes.c_uint32,
        }

    _fields_ = [
        ('field_pic_flag', ctypes.c_uint32, 1),
        ('is_intra', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('complementary_field_pair', ctypes.c_uint32, 1),
    ]
