import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('mono_chrome', ctypes.c_uint32, 1),
        ('color_range', ctypes.c_uint32, 1),
        ('separate_uv_delta_q', ctypes.c_uint32, 1),
        ('color_description_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1ColorConfig',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'mono_chrome': {'python_name': ['mono', 'chrome']},
        'color_range': {'python_name': ['color', 'range']},
        'separate_uv_delta_q': {'python_name': ['separate', 'uv', 'delta', 'q']},
        'color_description_present_flag': {'python_name': ['color', 'description', 'present', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
