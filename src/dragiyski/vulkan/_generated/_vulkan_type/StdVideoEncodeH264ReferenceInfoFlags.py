import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH264ReferenceInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'used_for_long_term_reference': {'python_name': ['used', 'for', 'long', 'term', 'reference']},
        'reserved': {'python_name': ['reserved']},
    }
}
