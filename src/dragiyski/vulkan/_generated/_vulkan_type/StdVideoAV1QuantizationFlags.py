import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1Quantization',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'using_qmatrix': {'python_name': ['using', 'qmatrix']},
        'diff_uv_delta': {'python_name': ['diff', 'uv', 'delta']},
        'reserved': {'python_name': ['reserved']},
    }
}
