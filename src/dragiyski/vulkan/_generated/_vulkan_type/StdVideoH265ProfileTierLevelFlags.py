import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('general_tier_flag', ctypes.c_uint32, 1),
        ('general_progressive_source_flag', ctypes.c_uint32, 1),
        ('general_interlaced_source_flag', ctypes.c_uint32, 1),
        ('general_non_packed_constraint_flag', ctypes.c_uint32, 1),
        ('general_frame_only_constraint_flag', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265ProfileTierLevel',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'general_tier_flag': {'python_name': ['general', 'tier', 'flag']},
        'general_progressive_source_flag': {'python_name': ['general', 'progressive', 'source', 'flag']},
        'general_interlaced_source_flag': {'python_name': ['general', 'interlaced', 'source', 'flag']},
        'general_non_packed_constraint_flag': {'python_name': ['general', 'non', 'packed', 'constraint', 'flag']},
        'general_frame_only_constraint_flag': {'python_name': ['general', 'frame', 'only', 'constraint', 'flag']},
    }
}
