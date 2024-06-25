import ctypes

class StdVideoEncodeH264ReferenceInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'used_for_long_term_reference': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]
