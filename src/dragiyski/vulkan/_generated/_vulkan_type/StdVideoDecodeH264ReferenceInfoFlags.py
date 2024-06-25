import ctypes

class StdVideoDecodeH264ReferenceInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'top_field_flag': ctypes.c_uint32,
            'bottom_field_flag': ctypes.c_uint32,
            'used_for_long_term_reference': ctypes.c_uint32,
            'is_non_existing': ctypes.c_uint32,
        }

    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]
