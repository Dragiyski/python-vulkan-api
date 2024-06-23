import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265ReferenceInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'used_for_long_term_reference': {'python_name': ['used', 'for', 'long', 'term', 'reference']},
        'unused_for_reference': {'python_name': ['unused', 'for', 'reference']},
        'reserved': {'python_name': ['reserved']},
    }
}
