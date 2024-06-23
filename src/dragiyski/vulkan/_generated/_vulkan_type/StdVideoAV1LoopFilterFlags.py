import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('loop_filter_delta_enabled', ctypes.c_uint32, 1),
        ('loop_filter_delta_update', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1LoopFilter',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'loop_filter_delta_enabled': {'python_name': ['loop', 'filter', 'delta', 'enabled']},
        'loop_filter_delta_update': {'python_name': ['loop', 'filter', 'delta', 'update']},
        'reserved': {'python_name': ['reserved']},
    }
}
