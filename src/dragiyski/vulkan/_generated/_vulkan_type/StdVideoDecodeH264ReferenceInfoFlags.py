import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoDecodeH264ReferenceInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'top_field_flag': {'python_name': ['top', 'field', 'flag']},
        'bottom_field_flag': {'python_name': ['bottom', 'field', 'flag']},
        'used_for_long_term_reference': {'python_name': ['used', 'for', 'long', 'term', 'reference']},
        'is_non_existing': {'python_name': ['is', 'non', 'existing']},
    }
}
