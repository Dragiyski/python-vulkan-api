import ctypes

class StdVideoAV1CDEF(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'cdef_damping_minus_3': ctypes.c_uint8,
            'cdef_bits': ctypes.c_uint8,
            'cdef_y_pri_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
            'cdef_y_sec_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
            'cdef_uv_pri_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
            'cdef_uv_sec_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
        }

    _fields_ = [
        ('cdef_damping_minus_3', ctypes.c_uint8),
        ('cdef_bits', ctypes.c_uint8),
        ('cdef_y_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_y_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ]
