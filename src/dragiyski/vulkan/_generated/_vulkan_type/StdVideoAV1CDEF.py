import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('cdef_damping_minus_3', ctypes.c_uint8),
        ('cdef_bits', ctypes.c_uint8),
        ('cdef_y_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_y_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'cdef_damping_minus_3': {'python_name': ['cdef', 'damping', 'minus', '3']},
        'cdef_bits': {'python_name': ['cdef', 'bits']},
        'cdef_y_pri_strength': {'python_name': ['cdef', 'y', 'pri', 'strength']},
        'cdef_y_sec_strength': {'python_name': ['cdef', 'y', 'sec', 'strength']},
        'cdef_uv_pri_strength': {'python_name': ['cdef', 'uv', 'pri', 'strength']},
        'cdef_uv_sec_strength': {'python_name': ['cdef', 'uv', 'sec', 'strength']},
    }
}
