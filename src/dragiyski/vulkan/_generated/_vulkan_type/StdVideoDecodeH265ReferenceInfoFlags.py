import ctypes

class StdVideoDecodeH265ReferenceInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'used_for_long_term_reference': ctypes.c_uint32,
            'unused_for_reference': ctypes.c_uint32,
        }

    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
    ]
